import random
import gym
import numpy as np
import collections
from tqdm import tqdm
import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt
import rl_utils

# ��ʵ��Ļ�����state��4ά����ֵ,action��2ά��ɢֵ
class ReplayBuffer:
    '''����طų�'''
    def __init__(self, capacity):
        self.buffer = collections.deque(maxlen=capacity) # ʹ�ö��д洢
    
    def add(self, state, action, reward, next_state, done): # done�ĺ����ǣ�
        self.buffer.append((state, action, reward, next_state, done))

    def sample(self, batch_size): # ��buffer�в���batch_size������
        transitions = random.sample(self.buffer, batch_size)
        state, action, reward, next_state, done = zip(*transitions) # ÿһ�����ձ�������һ��Ԫ��
        return np.array(state), action, reward, np.array(next_state), done
    
    def size(self): # ����Ŀǰbuffer�����ݵ�����
        return len(self.buffer)
    
class Qnet(torch.nn.Module):
    '''ֻ��һ�����ز�ļ�������,main-net��target-net����������ʵ��'''
    def __init__(self, state_dim, hidden_dim, action_dim): # ��ʼ����Ҫ״̬ά��/���ز�ά��/�ж�ά��
        super(Qnet, self).__init__()
        self.fc1 = torch.nn.Linear(state_dim, hidden_dim) # fcָȫ���Ӳ� full-connected
        self.fc2 = torch.nn.Linear(hidden_dim, action_dim)

    def forward(self, x):
        x = F.relu(self.fc1(x)) # ���ز�ʹ��ReLU�����,���������
        return self.fc2(x)
    
class Online_DQN:
    def __init__(self, state_dim, hidden_dim, action_dim, learning_rate, gamma, epsilon, target_update, device):
        self.action_dim = action_dim
        self.main_net = Qnet(state_dim, hidden_dim, self.action_dim).to(device)
        self.target_net = Qnet(state_dim, hidden_dim, self.action_dim).to(device)
        self.optimizer = torch.optim.Adam(self.main_net.parameters(), lr=learning_rate) # ʹ��Adam�Ż���(�Զ�����ѧϰ��)
        self.gamma = gamma
        self.epsilon = epsilon
        self.target_update = target_update # Ŀ���������Ƶ��
        self.count = 0 # ������,��¼��������
        self.device = device

    def take_action(self, state):
        if np.random.random() < self.epsilon:
            action = np.random.randint(self.action_dim)
        else:
            state = torch.tensor([state], dtype=torch.float).to(self.device) # ��state��װ��һ���б���Ϊ�˰�һά��������ת��Ϊ��ά����
            action = self.main_net(state).argmax().item() # .argmax()������Ǳ�������,��ʾ���ֵ���ڵ�����λ��,ͨ��.item()ת��Ϊint����
        return action
    
    def update(self, transition_dict): # transition_dict�Ǹ�ɶ�ģ�
        '''����һ�ε���,����main-net�Ĳ�������һ�θ���'''
        states = torch.tensor(transition_dict['states'], dtype=torch.float).to(self.device)
        actions = torch.tensor(transition_dict['actions']).view(-1,1).to(self.device) # �����γɵ�������Ԫ��ֵ����ĳ״̬�²�ȡ���ж�������
        rewards = torch.tensor(transition_dict['rewards'], dtype=torch.float).view(-1,1).to(self.device)                                                                
        next_states = torch.tensor(transition_dict['next_states'], dtype=torch.float).to(self.device)
        dones = torch.tensor(transition_dict['dones'], dtype=torch.float).view(-1,1).to(self.device)                                                                

        q_values = self.main_net(states).gather(1, actions) # ��������ȡqֵ
        max_next_q_values = self.target_net(next_states).max(1)[0].view(-1,1) # ��һ״̬�����Qֵ
        q_targets = rewards + self.gamma * max_next_q_values * (1-dones) # (1-dones)��ɶ������

        dqn_loss = torch.mean(F.mse_loss(q_values, q_targets))  # ���������ʧ����;mse_loss��������һ��(batch_size,1)��״������,����ÿ��Ԫ���Ƕ�Ӧ������ƽ�����;��ͨ��mean�������ֵ�õ����Ǳ���(��ά����)
        self.optimizer.zero_grad() # PyTorch��Ĭ���ݶ����ۻ���,������ÿ�η��򴫲�֮ǰ���ݶ�����
        dqn_loss.backward() # ���򴫲�������ʧ�����Ը�ģ�Ͳ������ݶ�
        self.optimizer.step() # ������һ��������ݶȸ���ģ�Ͳ���

        if self.count % self.target_update == 0:
            self.target_net.load_state_dict(self.main_net.state_dict())
        self.count += 1


if __name__ == '__main__':
    pass