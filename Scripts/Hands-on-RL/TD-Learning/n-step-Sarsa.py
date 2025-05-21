# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import os
from Sarsa import CliffWalkingEnv

class n_step_Sarsa:
    def __init__(self, ncol, nrow, nstep, alpha, gamma, epsilon, nactions=4) -> None:
        self.Q_table = np.zeros((nrow*ncol, nactions)) # 创建一个跟踪所有(s,a)pair的q值的表格
        self.nactions = nactions
        self.alpha = alpha # 学习率
        self.gamma = gamma # 计算G值(disconted return)时使用的折扣率
        self.epsilon = epsilon # ε-Greedy算法的参数
        self.nstep = nstep
        self.state_list = []
        self.action_list = []
        self.reward_list = []

    # def update_Q(self, s_t0, a_t0, r_list, s_list, a_list):
    #     TD_target = self.Q_table[s_list[-1],a_list[-1]]
    #     for i in reversed(range(self.nstep)):
    #         TD_target = self.gamma*TD_target + r_list[i]
    #     TD_error = self.Q_table[s_t0,a_t0] - TD_target
    #     self.Q_table[s_t0,a_t0] -= self.alpha*TD_error

    def update(self, s0, a0, r, s1, a1, done):
        self.state_list.append(s0)
        self.action_list.append(a0)
        self.reward_list.append(r)
        if len(self.state_list) == self.nstep:  # 若保存的数据可以进行n步更新
            G = self.Q_table[s1, a1]  # 得到Q(s_{t+n}, a_{t+n})
            for i in reversed(range(self.nstep)):
                G = self.gamma * G + self.reward_list[i]  # 不断向前计算每一步的回报
                # 如果到达终止状态,最后几步虽然长度不够n步,也将其进行更新
                if done and i > 0:
                    s = self.state_list[i]
                    a = self.action_list[i]
                    self.Q_table[s, a] += self.alpha * (G - self.Q_table[s, a])
            s = self.state_list.pop(0)  # 将需要更新的状态动作从列表中删除,下次不必更新
            a = self.action_list.pop(0)
            self.reward_list.pop(0)
            # n步Sarsa的主要更新步骤
            self.Q_table[s, a] += self.alpha * (G - self.Q_table[s, a])
        if done:  # 如果到达终止状态,即将开始下一条序列,则将列表全清空
            self.state_list = []
            self.action_list = []
            self.reward_list = []

    '''此函数根据当前的Q_table来决定在传入的状态下应采取什么行动
    充当的是policy improvement的作用,但是代码实现中并没有用一个变量来跟踪全程中策略的变化
    而仅仅是更新Q_table,最终策略也是根据最终Q_table的值来选择的deterministic策略'''
    def take_action(self, state):
        # if np.random.random() < self.nactions*self.epsilon/(self.nactions-1):
        if np.random.random() < self.epsilon:
            action = np.random.randint(self.nactions)
        else:
            action = np.argmax(self.Q_table[state])
        return action
    
    '''此函数用于训练完后打印最终策略'''
    def best_action(self,state):
        Q_max = np.max(self.Q_table[state])
        a = [0 for _ in  range(self.nactions)]
        for i in range(self.nactions):
            if self.Q_table[state,i] == Q_max: # 如果有多个action的q值并列最大也可以记录下来
                a[i] = 1
        return a
        
if __name__ == "__main__":
    # 实例化悬崖环境
    ncol = 12
    nrow = 4
    env = CliffWalkingEnv(ncol, nrow)
    # 设置随机种子
    np.random.seed(0)
    # 实例化使用n-step-Sarsa算法的agent
    epsilon = 0.1
    alpha = 0.1
    gamma = 0.9
    nstep = 7
    agent = n_step_Sarsa(ncol, nrow, nstep, alpha, gamma, epsilon)
    num_episodes = 5000 # 智能体在环境中运行的episode数量

    return_list = [] # 记录每个episode的return

    '''使用tqdm的进度条功能进行训练过程的可视化'''
    # for i in range(10): # 显示十个进度条
    #     with tqdm(total=int(num_episodes / 10), desc='Iteration %d' % i) as pbar:
    #         for i_episode in range (int(num_episodes/10)):
    #             episode_return = 0
    #             state = env.reset()
    #             current_state = state
    #             action = agent.take_action(state)
    #             current_action = action
    #             done = False
                
    #             for i in range(nstep):
    #                 # print('111')
    #                 next_state, reward, done = env.step(action)
    #                 next_action = agent.take_action(next_state)
    #                 episode_return += reward # 这个episode_return是用来可视化展示的，不需要折扣率
    #                 agent.action_list.append(next_action)
    #                 agent.state_list.append(next_state)
    #                 agent.reward_list.append(reward)
    #                 action = next_action

    #             while not done:
    #                 # print('222')
    #                 agent.update_Q(current_state, current_action, agent.reward_list, agent.state_list, agent.action_list)
    #                 current_state = agent.state_list.pop(0)
    #                 current_action = agent.action_list.pop(0)
    #                 next_state, reward, done = env.step(agent.action_list[-1])
    #                 next_action = agent.take_action(agent.state_list[-1])
    #                 episode_return += reward
    #                 agent.state_list.append(next_state)
    #                 agent.action_list.append(next_action)

    #             # 最后队列里还会剩余n个(s,a)pair的q值没有更新,单独处理一下

    #             TD_target = agent.Q_table[agent.state_list[-1],agent.action_list[-1]]
    #             for i in reversed(range(agent.nstep-1)):
    #                 TD_target = agent.gamma*TD_target + agent.reward_list[i]
    #                 TD_error = agent.Q_table[agent.state_list[i],agent.action_list[i]]
    #                 agent.Q_table -= agent.alpha*TD_error

    #             agent.action_list = []
    #             agent.state_list = []
    #             agent.reward_list = []

    for i in range(10):  # 显示10个进度条
        with tqdm(total=int(num_episodes / 10), desc='Iteration %d' % i) as pbar:
            for i_episode in range(int(num_episodes / 10)):  # 每个进度条的序列数
                episode_return = 0
                state = env.reset()
                action = agent.take_action(state)
                done = False
                while not done:
                    next_state, reward, done = env.step(action)
                    next_action = agent.take_action(next_state)
                    episode_return += reward  # 这里回报的计算不进行折扣因子衰减
                    agent.update(state, action, reward, next_state, next_action,
                                done)
                    state = next_state
                    action = next_action

                return_list.append(episode_return)
                # 每10个episode打印一下这10个episode的平均return
                if (i_episode + 1) % 10 == 0:  
                    pbar.set_postfix({
                        'episode':
                        '%d' % (num_episodes / 10 * i + i_episode + 1),
                        'return':
                        '%.3f' % np.mean(return_list[-10:])
                    })
                pbar.update(1)

    episodes_list = list(range(len(return_list)))
    plt.plot(episodes_list, return_list)
    plt.xlabel('Episodes')
    plt.ylabel('Returns')
    plt.title('{}-step Sarsa on {}'.format(nstep,'Cliff Walking'))
    plt.figtext(0.55, 0.95, "n={},ε={},α={},γ={},epi_num={}".format(nstep,epsilon,alpha,gamma,num_episodes),fontsize=10,color='red')
    # plt.show()
    plt.savefig("F:/王梓恒/学习资料/Machine_Learning/Reinforcement_Learnig/Scripts/Hands-on-RL/TD-Learning/n-step-Sarsa_results/n={},ε={},α={},γ={},epi_num={}.png".format(nstep,epsilon,alpha,gamma,num_episodes))


    def print_agent_to_file(agent, env, action_meaning, filename='n-step-Sarsa_results/output.txt', disaster=[], end=[]):
        # 自动创建目录（如果不存在）
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, 'a', encoding='utf-8') as f:
            for i in range(env.nrow):
                for j in range(env.ncol):
                    if (i * env.ncol + j) in disaster:
                        f.write('**** ')
                    elif (i * env.ncol + j) in end:
                        f.write('EEEE ')
                    else:
                        a = agent.best_action(i * env.ncol + j)
                        pi_str = ''
                        for k in range(len(action_meaning)):
                            pi_str += action_meaning[k] if a[k] > 0 else 'o'
                        f.write(pi_str + ' ')
                f.write('\n')
            f.write('\n')

    action_meaning = ['^', 'v', '<', '>']
    filename = 'n-step-Sarsa_results/output.txt'

    with open(filename, 'a', encoding='utf-8') as f:
        f.write('在参数n={},ε={},α={},γ={}下运行{}个episode, {}-step Sarsa算法最终收敛得到的策略为:\n'.format(nstep,epsilon,alpha,gamma,num_episodes,nstep))

    print_agent_to_file(agent, env, action_meaning, filename, list(range(37, 47)), [47])