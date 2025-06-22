import random
import gym
import numpy as np
import collections
from tqdm import tqdm
import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt
import rl_utils


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
    '''只有一层隐藏层的简单神经网络,这个是main-net还是target-net?'''
    def __init__(self, state_dim, hidden_dim, action_dim): # 初始化需要状态维数/隐藏层维数/行动维数
        super(Qnet, self).__init__()
        self.fc1 = torch.nn.Linear(state_dim, hidden_dim) # fc指全连接层 full-connected
        self.fc2 = torch.nn.Linear(hidden_dim, action_dim)

    def forward(self, x):
        x = F.relu(self.fc1(x)) # 隐藏层使用ReLU激活函数,引入非线性
        return self.fc2(x)
    
class Online_DQN:
    pass
