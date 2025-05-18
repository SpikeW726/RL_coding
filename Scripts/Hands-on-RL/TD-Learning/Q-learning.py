import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import os
from Sarsa import CliffWalkingEnv

class Online_Qlearning:
    '''On line架构的Q-learning算法'''
    def __init__(self, ncol, nrow, alpha, gamma, epsilon, nactions=4) -> None:
        self.Q_stable = np.zeros((nrow*ncol, nactions)) # 创建一个跟踪所有(s,a)pair的q值的表格
        self.nactions = nactions
        self.alpha = alpha # 学习率
        self.gamma = gamma # 计算G值(disconted return)时使用的折扣率
        self.epsilon = epsilon # ε-Greedy算法的参数

    def update_Q(self, s_t0, a_t0, r_t1, s_t1):
        TD_error = self.Q_stable[s_t0,a_t0] - (r_t1 + self.gamma*self.Q_stable[s_t1].max())
        self.Q_stable[s_t0,a_t0] -= self.alpha*TD_error

    '''此函数根据当前的Q_table来决定在传入的状态下应采取什么行动
    充当的是policy improvement的作用,但是代码实现中并没有用一个变量来跟踪全程中策略的变化
    而仅仅是更新Q_table,最终策略也是根据最终Q_table的值来选择的deterministic策略'''
    def take_action(self, state):
        #if np.random.random() < self.nactions*self.epsilon/(self.nactions-1):
        if np.random.random() < self.epsilon:
            action = np.random.randint(self.nactions)
        else:
            action = np.argmax(self.Q_stable[state])
        return action
    
    '''此函数用于训练完后打印最终策略'''
    def best_action(self,state):
        Q_max = np.max(self.Q_stable[state])
        a = [0 for _ in  range(self.nactions)]
        for i in range(self.nactions):
            if self.Q_stable[state,i] == Q_max: # 如果有多个action的q值并列最大也可以记录下来
                a[i] = 1
        return a
    
class Offline_Qlearning:
    '''Off line架构的Q-learning算法'''
    def __init__(self, ncol, nrow, alpha, gamma, epsilon, nactions=4) -> None:
        self.Q_stable = np.zeros((nrow*ncol, nactions)) # 创建一个跟踪所有(s,a)pair的q值的表格
        self.nactions = nactions
        self.alpha = alpha # 学习率
        self.gamma = gamma # 计算G值(disconted return)时使用的折扣率
        self.epsilon = epsilon # ε-Greedy算法的参数

    def update_Q(self, s_t0, a_t0, r_t1, s_t1):
        TD_error = self.Q_stable[s_t0,a_t0] - (r_t1 + self.gamma*self.Q_stable[s_t1].max())
        self.Q_stable[s_t0,a_t0] -= self.alpha*TD_error

    '''此函数根据当前的Q_table来决定在传入的状态下应采取什么行动
    充当的是policy improvement的作用,但是代码实现中并没有用一个变量来跟踪全程中策略的变化
    而仅仅是更新Q_table,最终策略也是根据最终Q_table的值来选择的deterministic策略'''
    def take_action(self, state):
        #if np.random.random() < self.nactions*self.epsilon/(self.nactions-1):
        if np.random.random() < self.epsilon:
            action = np.random.randint(self.nactions)
        else:
            action = np.argmax(self.Q_stable[state])
        return action
    
    '''此函数用于训练完后打印最终策略'''
    def best_action(self,state):
        Q_max = np.max(self.Q_stable[state])
        a = [0 for _ in  range(self.nactions)]
        for i in range(self.nactions):
            if self.Q_stable[state,i] == Q_max: # 如果有多个action的q值并列最大也可以记录下来
                a[i] = 1
        return a
    

if __name__ == "__main__":
    # 实例化悬崖环境
    ncol = 12
    nrow = 4
    env = CliffWalkingEnv(ncol, nrow)
    # 设置随机种子
    np.random.seed(0)
    # 实例化使用Sarsa算法的agent
    epsilon = 0.1
    alpha = 0.1
    gamma = 0.9
    agent = Online_Qlearning(ncol, nrow, alpha, gamma, epsilon)
    num_episodes = 5000 # 智能体在环境中运行的episode数量

    return_list = [] # 记录每个episode的return

    '''使用tqdm的进度条功能进行训练过程的可视化'''
    for i in range(10): # 显示十个进度条
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
    plt.title('Q-learning on {}'.format('Cliff Walking'))
    plt.figtext(0.6, 0.95, "ε={},α={},γ={},epi_num={}".format(epsilon,alpha,gamma,num_episodes),fontsize=10,color='red')
    # plt.show()
    plt.savefig("F:/王梓恒/学习资料/Machine_Learning/Reinforcement_Learnig/Scripts/Hands-on-RL/TD-Learning/Q-learning_results/ε={},α={},γ={},epi_num={}.png".format(epsilon,alpha,gamma,num_episodes))

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
        f.write('在参数ε={},α={},γ={}下运行{}个episode, Sarsa算法最终收敛得到的策略为:\n'.format(epsilon,alpha,gamma,num_episodes))

    print_agent_to_file(agent, env, action_meaning, filename, list(range(37, 47)), [47])