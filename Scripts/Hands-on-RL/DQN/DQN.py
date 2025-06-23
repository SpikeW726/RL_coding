import random
import gym
import numpy as np
import collections
from tqdm import tqdm
import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt
import rl_utils

# 本实验的环境中state是4维连续值,action是2维离散值
class ReplayBuffer:
    '''经验回放池'''
    def __init__(self, capacity):
        self.buffer = collections.deque(maxlen=capacity) # 使用队列存储
    
    def add(self, state, action, reward, next_state, done): # done的含义是？
        self.buffer.append((state, action, reward, next_state, done))

    def sample(self, batch_size): # 从buffer中采样batch_size个样本
        transitions = random.sample(self.buffer, batch_size)
        state, action, reward, next_state, done = zip(*transitions) # 每一个接收变量都是一个元组
        return np.array(state), action, reward, np.array(next_state), done
    
    def size(self): # 返回目前buffer中数据的数量
        return len(self.buffer)
    
class Qnet(torch.nn.Module):
    '''只有一层隐藏层的简单神经网络,main-net和target-net都是这个类的实例'''
    def __init__(self, state_dim, hidden_dim, action_dim): # 初始化需要状态维数/隐藏层维数/行动维数
        super(Qnet, self).__init__()
        self.fc1 = torch.nn.Linear(state_dim, hidden_dim) # fc指全连接层 full-connected
        self.fc2 = torch.nn.Linear(hidden_dim, action_dim)

    def forward(self, x):
        x = F.relu(self.fc1(x)) # 隐藏层使用ReLU激活函数,引入非线性
        return self.fc2(x)
    
class Online_DQN:
    def __init__(self, state_dim, hidden_dim, action_dim, learning_rate, gamma, epsilon, target_update, device):
        self.action_dim = action_dim
        self.main_net = Qnet(state_dim, hidden_dim, self.action_dim).to(device)
        self.target_net = Qnet(state_dim, hidden_dim, self.action_dim).to(device)
        self.optimizer = torch.optim.Adam(self.main_net.parameters(), lr=learning_rate) # 使用Adam优化器(自动调整学习率)
        self.gamma = gamma
        self.epsilon = epsilon
        self.target_update = target_update # 目标网络更新频率
        self.count = 0 # 计数器,记录迭代次数
        self.device = device

    def take_action(self, state):
        if np.random.random() < self.epsilon:
            action = np.random.randint(self.action_dim)
        else:
            state = torch.tensor([state], dtype=torch.float).to(self.device) # 将state包装成一个列表是为了把一维向量数据转化为二维张量
            action = self.main_net(state).argmax().item() # .argmax()输出的是标量张量,表示最大值所在的索引位置,通过.item()转化为int类型
        return action
    
    def update(self, transition_dict): # transition_dict是干啥的？
        '''进行一次迭代,即对main-net的参数进行一次更新'''
        states = torch.tensor(transition_dict['states'], dtype=torch.float).to(self.device)
        actions = torch.tensor(transition_dict['actions']).view(-1,1).to(self.device) # 这里形成的张量的元素值是在某状态下采取的行动的索引
        rewards = torch.tensor(transition_dict['rewards'], dtype=torch.float).view(-1,1).to(self.device)                                                                
        next_states = torch.tensor(transition_dict['next_states'], dtype=torch.float).to(self.device)
        dones = torch.tensor(transition_dict['dones'], dtype=torch.float).view(-1,1).to(self.device)                                                                

        q_values = self.main_net(states).gather(1, actions) # 根据索引取q值
        max_next_q_values = self.target_net(next_states).max(1)[0].view(-1,1) # 下一状态的最大Q值
        q_targets = rewards + self.gamma * max_next_q_values * (1-dones) # (1-dones)是啥？？？

        dqn_loss = torch.mean(F.mse_loss(q_values, q_targets))  # 均方误差损失函数;mse_loss函数返回一个(batch_size,1)形状的张量,其中每个元素是对应样本的平方误差;再通过mean函数求均值得到的是标量(零维张量)
        self.optimizer.zero_grad() # PyTorch中默认梯度是累积的,必须在每次反向传播之前将梯度清零
        dqn_loss.backward() # 反向传播计算损失函数对各模型参数的梯度
        self.optimizer.step() # 根据上一步计算的梯度更新模型参数

        if self.count % self.target_update == 0:
            self.target_net.load_state_dict(self.main_net.state_dict())
        self.count += 1


if __name__ == '__main__':
    pass