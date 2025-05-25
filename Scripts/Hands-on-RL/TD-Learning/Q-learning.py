import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import os
import random
from Sarsa import CliffWalkingEnv

class Online_Qlearning:
    '''On line架构的Q-learning算法'''
    def __init__(self, ncol, nrow, alpha, gamma, epsilon, nactions=4) -> None:
        self.Q_table = np.zeros((nrow*ncol, nactions)) # 创建一个跟踪所有(s,a)pair的q值的表格
        self.nactions = nactions
        self.alpha = alpha # 学习率
        self.gamma = gamma # 计算G值(disconted return)时使用的折扣率
        self.epsilon = epsilon # ε-Greedy算法的参数

    def update_Q(self, s_t0, a_t0, r_t1, s_t1):
        TD_error = self.Q_table[s_t0,a_t0] - (r_t1 + self.gamma*self.Q_table[s_t1].max())
        self.Q_table[s_t0,a_t0] -= self.alpha*TD_error

    '''此函数根据当前的Q_table来决定在传入的状态下应采取什么行动
    充当的是policy improvement的作用,但是代码实现中并没有用一个变量来跟踪全程中策略的变化
    而仅仅是更新Q_table,最终策略也是根据最终Q_table的值来选择的deterministic策略'''
    def take_action(self, state):
        #if np.random.random() < self.nactions*self.epsilon/(self.nactions-1):
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
    
class Offline_Qlearning:
    '''Off line架构的Q-learning算法'''
    def __init__(self, ncol, nrow, alpha, gamma, epsilon, nactions=4) -> None:
        self.Q_table = np.zeros((nrow*ncol, nactions)) # 创建一个跟踪所有(s,a)pair的q值的表格
        self.episode_buffer = []
        self.nactions = nactions
        self.alpha = alpha # 学习率
        self.gamma = gamma # 计算G值(disconted return)时使用的折扣率
        self.epsilon = epsilon # ε-Greedy算法的参数

    def collect_experience(self, env, num_episodes):
        # 使用随机策略收集数据
        for _ in range(num_episodes):
            state = env.reset()
            done = False
            while not done:
                action = self.take_action(state)
                next_state, reward, done = env.step(action)
                self.episode_buffer.append((state, action, reward, next_state))
                state = next_state

    def batch_update_Q(self, batch_size): # 共更新Q值epochs次,每次在采样num_episodes次收集到的所有(s0,a0,r1,s1)集中抽取batch_size个数据
        batch = random.sample(self.episode_buffer, batch_size)
        for s_t0, a_t0, r_t1, s_t1 in batch:
            TD_error = self.Q_table[s_t0,a_t0] - (r_t1 + self.gamma*self.Q_table[s_t1].max())
            self.Q_table[s_t0,a_t0] -= self.alpha*TD_error

    '''此函数根据Behavior policy来采取行动生成episode
    这里采取的Behavior policy就是每个action等概率随机'''
    def take_action(self, state):
        action = np.random.randint(self.nactions)
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
    # 实例化使用Q-Learning算法的agent
    epsilon = 0.1
    alpha = 0.1
    gamma = 0.9
    # off-line策略特有的参数
    is_offline = True
    off_batch = 32
    off_epoch = 300

    if not is_offline:
        agent = Online_Qlearning(ncol, nrow, alpha, gamma, epsilon)
    else: agent = Offline_Qlearning(ncol, nrow, alpha, gamma, epsilon)
    num_episodes = 500 # 智能体在环境中运行的episode数量

    return_list = [] # 记录每个episode的return

    '''使用tqdm的进度条功能进行训练过程的可视化'''
    for i in range(10): # 显示十个进度条
        if not is_offline:
            with tqdm(total=int(num_episodes / 10), desc='Iteration %d' % i) as pbar: 
                for i_episode in range (int(num_episodes/10)):
                    episode_return = 0
                    state = env.reset()
                    action = agent.take_action(state)
                    done = False
                    
                    while not done:
                        next_state, reward, done = env.step(action)
                        episode_return += reward # 这个episode_return是用来可视化展示的，不需要折扣率
                        agent.update_Q(state, action, reward, next_state)
                        action = agent.take_action(next_state)
                        state = next_state

                    return_list.append(episode_return)
                    # 每num_episodes/10个episode打印一下这10个episode的平均return
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
            plt.title('Offline Q-learning on {}'.format('Cliff Walking'))
            plt.figtext(0.6, 0.95, "ε={},α={},γ={},epi_num={}".format(epsilon,alpha,gamma,num_episodes),fontsize=10,color='red')
            # plt.show()
    
        else:
            with tqdm(total=int(off_epoch / 10), desc='Iteration %d' % i) as pbar:
                agent.collect_experience(env, num_episodes)
                for i in range(off_epoch):
                    agent.batch_update_Q(off_batch)
                    if (i+1) % 10 == 0:
                        pbar.set_postfix({
                            'episode':
                            '%d' % (off_epoch / 10 * i + i + 1)
                        })
                    pbar.update(1)






    if is_offline:
        # plt.savefig("F:/王梓恒/学习资料/Machine_Learning/Reinforcement_Learnig/Scripts/Hands-on-RL/TD-Learning/Q-learning_results/Offline,ε={},α={},γ={},epi_num={}.png".format(epsilon,alpha,gamma,num_episodes))
        pass
    else:
        plt.savefig("F:/王梓恒/学习资料/Machine_Learning/Reinforcement_Learnig/Scripts/Hands-on-RL/TD-Learning/Q-learning_results/Online,ε={},α={},γ={},epi_num={}.png".format(epsilon,alpha,gamma,num_episodes))


    def print_agent_to_file(agent, env, action_meaning, filename='Q-learning_results/output.txt', disaster=[], end=[]):
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
    filename = 'Q-learning_results/output.txt'

    with open(filename, 'a', encoding='utf-8') as f:
        if is_offline:
            f.write('在参数ε={},α={},γ={}下运行{}个episode, 用{}个batch_size为{}的epoch训练, offline Q-Learning算法最终收敛得到的策略为:\n'.format(epsilon,alpha,gamma,num_episodes,off_epoch,off_batch))
        else:
            f.write('在参数ε={},α={},γ={}下运行{}个episode, Online Q-Learning算法最终收敛得到的策略为:\n'.format(epsilon,alpha,gamma,num_episodes))

    print_agent_to_file(agent, env, action_meaning, filename, list(range(37, 47)), [47])