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
    '''ֻ��һ�����ز�ļ�������,�����main-net����target-net?'''
    def __init__(self, state_dim, hidden_dim, action_dim): # ��ʼ����Ҫ״̬ά��/���ز�ά��/�ж�ά��
        super(Qnet, self).__init__()
        self.fc1 = torch.nn.Linear(state_dim, hidden_dim) # fcָȫ���Ӳ� full-connected
        self.fc2 = torch.nn.Linear(hidden_dim, action_dim)

    def forward(self, x):
        x = F.relu(self.fc1(x)) # ���ز�ʹ��ReLU�����,���������
        return self.fc2(x)
    
class Online_DQN:
    pass
