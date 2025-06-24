# Math Basis for R-L

## Overall



<img src="C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250309225802756.png" alt="image-20250309225802756" style="zoom: 67%;" />

## Chapter-1 Basic Concepts

### State

The status of the agent with respect to the environment.  智能体关于环境的状态

For the grid-world example, the location of the agent is the state. There are 9 possible locations and hence 9 states $s_1,s_2,......,s_9$ 

<img src="C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250309233029848.png" alt="image-20250309233029848" style="zoom:80%;" />

### State space

The ==set== of all states $S=\{s_i\}_{i=1}^9$  所有状态的==集合==

### Action

For each state, there are 5 possible actions: $a_1, ... ,a_5$

<img src="data:image/png;base64,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" alt="img" style="zoom: 80%;" />

### Action space of a state

The set of all possible actions of a state: $\mathcal{A}(s_i)=\{a_i\}_{i=1}^5$

注意行动空间==是状态的函数==，不同状态对应的行动空间不同

### State transition

When taking an action, the agent may move from one state to another. Such a process is called ***state transition***. State transition defines the interaction with the environment.  由一个状态到另一个状态的过程

At state $s_1$ , if we choose action $a_2$ , then what is the next state?  $s_1\xrightarrow{a_2}s_2$

Tabular representation: We can use a table to describe the state transition

<img src="C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250309234636841.png" alt="image-20250309234636841" style="zoom:80%;" />

Can only represent ***deterministic*** cases.  只能用于记录***确定性***的情况，故不常用

State transition probability: use probability to describe state transition ==**更常用**==

​	Intuition: At state $s_1$ , if we choose action $a_2$ , the next state is $s_2$.

​	Math: 如果现在处于 $s_1$，然后采取 $a_2$ ，那么下一个状态为 $s_2$ 的概率为1，为其他状态的概率为0
$$
\begin{aligned}&p(s_{2}|s_{1},a_{2})=1\\&p(s_{i}|s_{1},a_{2})=0\quad\forall i\neq2\end{aligned}
$$
Here it is a ***deterministic*** case. The state transition could be ***stochastic (more often)***.

### Policy

It tells the what actions to take at a state.  **策略**告诉智能体位于什么状态时应该采取什么行动

**Intuitive representation:** The arrows demonstrate a policy

<img src="data:image/png;base64,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" alt="img" style="zoom:80%;" />

Based on this policy, we get the following paths with different starting points.

<img src="C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250309235945946.png" alt="image-20250309235945946" style="zoom:80%;" />

**Mathematical representation**: using conditional probability 使用条件概率
$$
\begin{gathered}\pi(a_{1}|s_{1})=0\\\pi(a_{2}|s_{1})=1\\\pi(a_{3}|s_{1})=0\\\pi(a_{4}|s_{1})=0\\\pi(a_{5}|s_{1})=0\end{gathered}
$$
At $s_1$ , the probability of taking $a_2$ is $1$ . It's a ***deterministic*** policy.

There are also ***stochastic*** policies:

<img src="C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250310000414023.png" alt="image-20250310000414023" style="zoom:80%;" />

In this policy, for $s_1$ :
$$
\begin{aligned}&\pi(a_{1}|s_{1})=0\\&\pi(a_{2}|s_{1})=0.5\\&\pi(a_{3}|s_{1})=0.5\\&\pi(a_{4}|s_{1})=0\\&\pi(a_{5}|s_{1})=0\end{aligned}
$$
**Tabular representation** of a policy:

<img src="C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250310000842343.png" alt="image-20250310000842343" style="zoom:80%;" />

Can represent either ***deterministic*** or ***stochastic*** cases.

### Reward

A real number we get **after an action**. 采取行动后得到的一个实数/标量

Reward can be interpreted as a **human interface**. 

我们可以把Reward当作一种**人机交互**的方法，我们可以通过设计reward来引导机器人完成我们期望的行为

In the grid-world example, the rewards are designed as follows:
$\bullet$ If the agent attempts to get out of the boundary, let $r_\mathrm{bound}=-1$
$\bullet$ If the agent attempts to enter a forbidden cell, let $r_\mathrm{forbid}=-1$
$\bullet$ If the agent reaches the target cell, Iet $r_\mathrm{target}=+1$
$\bullet$ Otherwise, the agent gets a reward of $r=0.$

**Mathematical description**: conditional probability

$\bullet$ Intuition: At state $s_1$ , if we choose action $a_1$ , the reward is $-1$ 

$\bullet$ Math: $p(r=-1 |s_1,a_1) =1$ and $p(r\neq-1 |s_1,a_1) =0$ 

The reward depends on the state and action, ==but not the next state.==  Reward只取决于当前的状态及采取的行动，并==不取决于下一状态==

### Trajectory and return

A ***trajectory*** is a state-action chain:
$$
s_1\xrightarrow{a_2}s_2\xrightarrow{a_3}s_5\xrightarrow{a_3}s_8\xrightarrow{a_2}s_9
$$
The ***return*** of this trajectory is the sum of all the rewards collected along the trajectory:
$$
return = 0+0+0+1 = 1
$$
Different ***policies*** lead to different ***trajectory*** and different ***return*** 

Return could be used to evaluate a policy is good or not.

### Discounted return

<img src="C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250310223025317.png" alt="image-20250310223025317" style="zoom:80%;" />

A trajectory may be infinite:
$$
s_1\xrightarrow{a_2}s_2\xrightarrow{a_3}s_5\xrightarrow{a_3}s_8\xrightarrow{a_2}s_9\xrightarrow{a_5}s_9\xrightarrow{a_5}s_9\ldots
$$
The return is

$$
\text{return}=0+0+0+1+1+1+\cdots=\infty
$$
The definition is invalid since the return diverges.  由于return值是发散的，这个轨迹/策略的定义是无效的

Introduce a discount rate $\gamma\in[0,1)$

***Discounted return***:
$$
\begin{aligned}discounted\ return&=0+\gamma0+\gamma^{2}0+\gamma^{3}1+\gamma^{4}1+\gamma^{5}1+\ldots
\\&=\gamma^3(1+\gamma+\gamma^2+\ldots)=\gamma^3\frac{1}{1-\gamma}\end{aligned}
$$
Benefits: 1) The sum becomes finite

​                 2) Balance the far and near future rewards  ==如果$\gamma$ 趋近$0$，则更加注重最近的reward；如果$\gamma$ 趋近  于 $1$ ，则更加注重长远的reward==

### Episode

 When interacting with the environment following a policy, the agent may stop at some ***terminal state***

The resulting trajectory is called an ***episode*** or ***trial***  ==有限的==轨迹才被称作*episode* 

Tasks with episodes are called ***episodic tasks*** 

Some tasks may have no terminal states, meaning the interaction with the environment will never end. Such tasks are called ***continuing tasks***.   没有终止状态、与环境无限交互的任务

In fact, we can treat episodic and continuing tasks in a ***unified mathematical way*** by ==converting episodic tasks to continuing tasks.==

$\bullet$ Option 1: Treat the target state as a special *absorbing state*. Once the agent reaches an absorbing state, it will never leave. The consequent rewards $r=0.$  智能体进入目标状态后就无法再跳出，后续reward全为0
$\bullet$ Option 2: Treat the target state as a normal state with a policy. The agent can still leave the target state and gain $r=+1$ when entering the target state.  智能体进入目标区域后reward不断+1，并且还可以跳出

### Markov decision process (MDP)

Key elements of MDP:

$\bullet$ Sets:

​	$\bullet$ State: the set of states $S$
​	$\bullet$ Action: the set of actions $\mathcal{A}(s)$ is associated for state $s\in\mathcal{S}.$
​	$\bullet$ Reward: the set of rewards $\mathcal{R}(s,a).$
$\bullet$ Probability distribution:
​	$\bullet$ State transition probability: at state $s$, taking action $a$, the probability to transit to state $s^\prime$ is $p(s^\prime|s,a)$
​	$\bullet$ Reward probability: at state $s$, taking action $a$, the probability to get reward $r$ is $p(r|s,a)$
$\bullet$ Policy: at state $s$, the probability to choose action $a$ is $\pi(a|s)$
$\bullet$ Markov property: ***memoryless*** property  ==未来状态仅依赖于当前状态，与过去状态无关==
$$
\begin{aligned}&p(s_{t+1}|a_{t+1},s_t,\ldots,a_1,s_0)=p(s_{t+1}|a_{t+1},s_t),\\&p(r_{t+1}|a_{t+1},s_t,\ldots,a_1,s_0)=p(r_{t+1}|a_{t+1},s_t).\end{aligned}
$$
***Markov decision process*** becomes ***Markov process*** once the policy is given.

## Chapter-2 Bellman Equation

### Motivating examples

Calculating return is important to evaluate a policy.

***How to calculate return?***

<img src="C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250310233150114.png" alt="image-20250310233150114" style="zoom:80%;" />

Method 1: by definition

Let $v_{i}$ denote the return obtained starting from $s_i\left(i=1,2,3,4\right)$
$$
v_{1}=r_1+\gamma r_2+\gamma^2r_3+\ldots\\v_{2}=r_2+\gamma r_3+\gamma^2r_4+\ldots\\v_{3}=r_3+\gamma r_4+\gamma^2r_1+\ldots\\v_{4}=r_4+\gamma r_1+\gamma^2r_2+\ldots
$$
Method 2: The returns rely on each other  ==Bootstrapping==
$$
v_{1}=r_1+\gamma(r_2+\gamma r_3+\ldots)=r_1+\gamma v_2\\v_{2}=r_2+\gamma(r_3+\gamma r_4+\ldots)=r_2+\gamma v_3\\v_{3}=r_3+\gamma(r_4+\gamma r_1+\ldots)=r_3+\gamma v_4\\v_{4}=r_4+\gamma(r_1+\gamma r_2+\ldots)=r_4+\gamma v_1
$$
Write in the matrix-vector form:
$$
\left.\underbrace{\left[\begin{array}{c}v_1\\v_2\\v_3\\v_4\end{array}\right]}_{\mathbf{v}}=\left[\begin{array}{c}r_1\\r_2\\r_3\\r_4\end{array}\right]\right.+\begin{bmatrix}\gamma v_2\\\gamma v_3\\\gamma v_4\\\gamma v_1\end{bmatrix}=\underbrace{\begin{bmatrix}r_1\\r_2\\r_3\\r_4\end{bmatrix}}_{\mathbf{r}}+\underbrace{\gamma\begin{bmatrix}0&1&0&0\\0&0&1&0\\0&0&0&1\\1&0&0&0\end{bmatrix}}_{\mathbf{P}}\underbrace{\begin{bmatrix}v_1\\v_2\\v_3\\v_4\end{bmatrix}}_{\mathbf{v}}
$$
which can be rewritten and solved as:
$$
\mathbf{v}=\mathbf{r}+\gamma\mathbf{Pv}\\\mathbf{v}=(\mathbf{I}-\gamma\mathbf{P})^{-1}\mathbf{r}
$$
This is the Bellman equation ==(for this specific deterministic problem)!!== 

$\bullet$ Though simple, it demonstrates the core idea: **the value of one state relies on the values of other states.**
$\bullet$ A matrix-vector form is more clear to see how to solve the state values

### State value

Consider the following single-step process:
$$
S_t\xrightarrow{A_t}R_{t+1},S_{t+1}
$$

$\bullet$ $t, t+ 1:$ discrete time instances  

$\bullet\  S_t{:}$ state at time $t$
$\bullet \ A_t$: the action taken at state $S_t$
$\bullet\  R_{t+1}$: the reward obtained after taking $A_t$ 注意这个下标习惯性写为$t+1$ 但是这个值只由 $t$ 时刻的量决定

$\bullet \ S_{t+1}\colon$ the state transited to after taking $A_t$ 

Note that $S_t,A_t,R_{t+1}$ are all random variables  全是**随机变量**，后续可进行求期望、方差等操作

This step is governed by the following probability distributions:
$\bullet$ $S_t\to A_t$ is governed by $\pi(A_t=a|S_t=s)$
$\bullet$ $S_t, A_t\to R_{t+ 1}$ is governed by $p(R_t+1=r|S_t=s,A_t=a)$ 

$\bullet$ $S_t, A_t\to S_{t+ 1}$ is governed by $p(S_t+1=s^\prime|S_t=s,A_t=a)$

Consider the folowing multi-step trajectory:
$$
S_t\xrightarrow{A_t}R_{t+1},S_{t+1}\xrightarrow{A_{t+1}}R_{t+2},S_{t+2}\xrightarrow{A_{t+2}}R_{t+3},\ldots
$$
The discounted return is:
$$
G_t=R_{t+1}+\gamma R_{t+2}+\gamma^2R_{t+3}+\ldots
$$
$\bullet\ \gamma \in [ 0, 1)$ is a discount rate

$\bullet\ G_t$ is also a random variable since $R_t+1,R_{t+2},\ldots$ are all random variables.   ***Disconted return*** 也是随机变量

The ==***expectation***== of $G_t$ is defined as the ==***state value***==:
$$
v_\pi(s)=\mathbb{E}[G_t|S_t=s]
$$
<img src="C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250311113226069.png" alt="image-20250311113226069" style="zoom:80%;" />

### Bellman equation

#### Derivation

Consider a random trajectory:
$$
S_t\xrightarrow{A_t}R_{t+1},S_{t+1}\xrightarrow{A_{t+1}}R_{t+2},S_{t+2}\xrightarrow{A_{t+2}}R_{t+3},\ldots
$$
The discounted return $G_t$ can be written as:
$$
\begin{aligned}G_{t}&=R_{t+1}+\gamma R_{t+2}+\gamma^{2}R_{t+3}+\ldots,\\&=R_{t+1}+\gamma(R_{t+2}+\gamma R_{t+3}+\ldots),\\&=R_{t+1}+\gamma G_{t+1},\end{aligned}
$$
 Then, it follows from the definition of the ==**state value**== that
$$
\begin{aligned}v_\pi(s)&=\mathbb{E}[G_t|S_t=s]\\&=\mathbb{E}[R_{t+1}|S_t=s]+\gamma \mathbb{E}[G_{t+1}|S_t=s]\end{aligned}
$$
First, calculate the first term:
$$
\begin{aligned}\mathbb{E}[R_{t+1}|S_t=s]&=\sum_a\pi(a|s)\mathbb{E}[R_{t+1}|S_t=s,A_t=a]\\&=\sum_a\pi(a|s)\sum_rp(r|s,a)r\end{aligned}
$$
上式中 $\pi(a|s)$ 为确定当前状态为 $s$ 时采取行动 $a$ 的概率， $p(r|s,a)$ 为确定当前状态为 $s$ 以及采取行动 $a$ 之后得到的 $reward$ 值为 $r$ 的概率

Second, calculate the second term:

$$
\begin{aligned}\mathbb{E}[G_{t+1}|S_t=s]&=\sum_{s'}\mathbb{E}[G_{t+1}|S_t=s,S_{t+1}=s']p(s'|s)\\&=\sum_{s'}\mathbb{E}[G_{t+1}|S_{t+1}=s']p(s'|s)\\&=\sum_{s'}v_\pi(s')p(s'|s)\\&=\sum_{s'}v_\pi(s')\sum_ap(s'|s,a)\pi(a|s)\end{aligned}
$$
其中第二步的化简是因为==根据马尔可夫性质，t+1的状态确定后，t的状态就对后续无影响了==

Therefore, we have:
$$
\begin{aligned}v_{\pi}(s)&=\mathbb{E}[R_{t+1}|S_{t}=s]+\gamma\mathbb{E}[G_{t+1}|S_{t}=s],\\&=\underbrace{\sum_a\pi(a|s)\sum_rp(r|s,a)r}_{\text{mean of immediate rewards}}+\underbrace{\gamma\sum_a\pi(a|s)\sum_{s^{\prime}}p(s^{\prime}|s,a)v_\pi(s^{\prime}),}_{\text{mean of future rewards}}\\&=\sum_{a}\pi(a|s)\left[\sum_{r}p(r|s,a)r+\gamma\sum_{s^{\prime}}p(s^{\prime}|s,a)v_{\pi}(s^{\prime})\right],\quad\forall s\in\mathcal{S}.\end{aligned}
$$
注意：

1. 上式便为==贝尔曼公式==，**描述了不同状态下值函数(state value)之间的关系**
2. 它由两项组成，一项是immediate reward，一项是future reward
3. 注意最后的 $\forall s\in\mathcal{S}$ , 这代表贝尔曼方程不是一个方程而是一组方程，对于==状态空间中的每个状态==都有一个上述形式的方程
4. $\pi(a|s)$ 是一个给定的策略policy，解这个方程就叫做==策略评估**policy evaluation**==
5. $p(s'|s,a)$ 和 $p(r|s,a)$ 是否已知取决于模型是否已知，若未知则对应后续课程将讨论的model-free reinforcement learning

#### Matrix-vector form and solution

Rewrite the Bellman equation as:
$$
v_\pi(s)=r_\pi(s)+\gamma\sum_{s^{\prime}}p_\pi(s^{\prime}|s)v_\pi(s^{\prime})
$$
where
$$
r_{\pi}(s)\triangleq\sum_{a}\pi(a|s)\sum_{r}p(r|s,a)r,\quad p_{\pi}(s^{\prime}|s)\triangleq\sum_{a}\pi(a|s)p(s^{\prime}|s,a)
$$
$r_\pi(s)$ 代表==在 $s$ 状态下immediate reward的平均值==

将所有状态编号记作 $s_i(i=1,\dots,n)$ 对于状态 $s_i$ ,贝尔曼公式记作 $v_\pi(s_i)=r_\pi(s_i)+\gamma\sum_{s_j}p_\pi(s_j|s_i)v_\pi(s_j)$

Put all these quations for all the states together and rewrite to a ==matrix-vector form==:
$$
\color{red}v_{\pi}=r_{\pi}+\gamma P_{\pi}v_{\pi}\quad 贝尔曼公式的向量形式
$$
where
$$
\begin{aligned}\quad&\bullet v_{\pi}=[v_{\pi}(s_{1}),\ldots,v_{\pi}(s_{n})]^{T}\in\mathbb{R}^{n}\\&\bullet r_{\pi}=[r_{\pi}(s_{1}),\ldots,r_{\pi}(s_{n})]^{T}\in\mathbb{R}^{n}\\&\bullet P_{\pi}\in\mathbb{R}^{n\times n},\mathrm{~where~}[P_{\pi}]_{ij}=p_{\pi}(s_{j}|s_{i}),\text{ is the state transition matrix}\end{aligned}
$$
If there are 4 states:
$$
\underbrace{\begin{bmatrix}v_\pi(s_1)\\v_\pi(s_2)\\v_\pi(s_3)\\v_\pi(s_4)\end{bmatrix}}_{v_\pi}=\underbrace{\begin{bmatrix}r_\pi(s_1)\\r_\pi(s_2)\\r_\pi(s_3)\\r_\pi(s_4)\end{bmatrix}}_{r_\pi}+\underbrace{\gamma\begin{bmatrix}p_\pi(s_1|s_1)&p_\pi(s_2|s_1)&p_\pi(s_3|s_1)&p_\pi(s_4|s_1)\\p_\pi(s_1|s_2)&p_\pi(s_2|s_2)&p_\pi(s_3|s_2)&p_\pi(s_4|s_2)\\p_\pi(s_1|s_3)&p_\pi(s_2|s_3)&p_\pi(s_3|s_3)&p_\pi(s_4|s_3)\\p_\pi(s_1|s_4)&p_\pi(s_2|s_4)&p_\pi(s_3|s_4)&p_\pi(s_4|s_4)\end{bmatrix}}_{P_\pi}\underbrace{\begin{bmatrix}v_\pi(s_1)\\v_\pi(s_2)\\v_\pi(s_3)\\v_\pi(s_4)\end{bmatrix}}_{v_\pi}.
$$

#### Solve state values

Why to solve state values?

​	Given a policy, finding out the corresponding state values is called ==***policy evaluation***== It's a fundamantal problem in R-L. It's the foundation to find better policies.

The *closed-form* solution is:
$$
\mathbf{v}_\pi=(\mathbf{I}-\gamma\mathbf{P}_\pi)^{-1}\mathbf{r}_\pi
$$
但在实际应用中并不会用这种方式求解，因为高位矩阵求逆过于复杂

An *iterative solution* is:
$$
v_{k+1}=r_k+\gamma P_{\pi}v_k
$$
初始随机代入一个值 $v_0$ , 然后通过迭代计算出序列 $\{v_0,v_1,v_2,\dots\}$

而我们可以证明 $v_k\to v_\pi=(I-\gamma P_\pi)^{-1}r_\pi,\quad k\to\infty$

故通过任意初始值的迭代法可以计算出每个状态下的state value值

<img src="C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250313213320824.png" alt="image-20250313213320824" style="zoom:80%;" />

### Action value

From state value to action value:
	State value: the average return the agent can get starting from a state
	Action value: the average return the agent can get starting from a state and taking an action.

Definition:
$$
q_\pi(s,a)=\mathbb{E}[G_t|S_t=s,A_t=a]
$$
​	$q_\pi(s,a)$ is a function of the state-action pair $(s,a)$

​	$q_\pi(s,a)$ depends on $\pi$ 

It follows from the properties of conditional expectation that
$$
\underbrace{\mathbb{E}[G_t|S_t=s]}_{\color{red}v_\pi(s)}=\sum_a\underbrace{\mathbb{E}[G_t|S_t=s,A_t=a]}_{\color{red}q_\pi(s,a)}\pi(a|s)
$$
Hence, the relationship between state value and action value:
$$
{\color{red}v_\pi(s)}=\sum_a\pi(a|s){\color{red}q_\pi(s,a)}\quad(1)
$$
Recall that the state value is given by
$$
v_{\pi}(s)=\sum_{a}\pi(a|s)\underbrace{\left[\sum_{r}p(r|s,a)r+\gamma\sum_{s^{\prime}}p(s^{\prime}|s,a)v_{\pi}(s^{\prime})\right]}_{\color{red}q_{\pi}(s,a)}
$$
与 Bellman equation-Derivation 章节推导的state value表达式比较可得action value的公式：
$$
{\color{red}q_\pi(s,a)}=\sum_rp(r|s,a)r+\gamma\sum_{s^{\prime}}p(s^{\prime}|s,a){\color{red}v_\pi(s^{\prime})}\quad(2)
$$
$s^{\prime}$ 是在状态 $s$ 下采取行动 $a$ 后到达的状态

$(1)$ and $(2)$ are the 2 sides of the same coin:

​	$(1)$ shows how to obtain state values from action values

​	$(2)$ shows how to obtain action values from state values

将 state value 形式的贝尔曼方程代入（2）中可以得到 action value 形式的贝尔曼方程：
$$
q_\pi(s,a)=\sum_{r\in\mathcal{R}}p(r|s,a)r+\gamma\sum_{s^{\prime}\in\mathcal{S}}p(s^{\prime}|s,a)\sum_{a^{\prime}\in\mathcal{A}(s^{\prime})}\pi(a^{\prime}|s^{\prime})q_\pi(s^{\prime},a^{\prime})
$$
Example:

<img src="C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250313221509089.png" alt="image-20250313221509089" style="zoom:80%;" />

Write out the action values for state $s_1$ :
$$
q_\pi(s_1,a_2)=-1+\gamma v_\pi(s_2)
$$
Questions: $q_{\pi}(s_{1},a_{1}),q_{\pi}(s_{1},a_{3}),q_{\pi}(s_{1},a_{4}),q_{\pi}(s_{1},a_{5})=?$

$q_\pi$ 与 $v_\pi$ 相比少乘一个 $p(a|s)$ 所以就算既定策略规定在 $s_1$ 状态必然采取 $a_2$ 行动，这并不代表着其他行动的action value就一定为 $0$ 
$$
\begin{aligned}&q_{\pi}(s_{1},a_{1})=-1+\gamma v_{\pi}(s_{1}),\\&q_{\pi}(s_{1},a_{3})=0+\gamma v_\pi(s_3),\\&q_{\pi}(s_{1},a_{4})=-1+\gamma v_\pi(s_1),\\&q_{\pi}(s_{1},a_{5})=0+\gamma v_\pi(s_1).\end{aligned}
$$


### Summary

![image-20250313221417016](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250313221417016.png)

## Chapter-3 Bellman Optimality Equation

### Motivating examples

<img src="F:\新建文件夹\WeChat Files\wxid_ygzltfcqkee422\FileStorage\Temp\1741875889280.png" alt="1741875889280" style="zoom:80%;" />

<img src="F:\新建文件夹\WeChat Files\wxid_ygzltfcqkee422\FileStorage\Temp\1741876138652.png" alt="1741876138652" style="zoom:80%;" />

A new policy is obtained:
$$
\left.\pi_{\mathrm{new}}(a|s_{1})=\left\{\begin{array}{ll}1&a=a^{*}\\0&a\neq a^{*}\end{array}\right.\right.\\\mathrm{where~}a^{*}=\arg\max_{a}q_{\pi}(s_{1},a)=a_{3}.
$$
Why doing this can improve the policy?

​	Intuition: action values can be used to evaluate actions.

​	Math: nontrivial and will be introduced in this lecture

### Definition of Optimal Policy

The state value could be used to evaluate if a policy is good or not:
$$
if\quad v_{\pi_1}(s)\geq v_{\pi_2}(s)\quad\mathrm{for~all}s\in\mathcal{S}
$$
then $\pi_1$ is "better" than $\pi_2$ 

Definition:

​	A policy $\pi^{*}$ is optimal if $v_{\pi^{*}}(s)\geq v_{\pi}(s)$ for ==all $s$ and for other policy $\pi$==

引出许多问题：最优策略是否一定存在？是否是唯一的？是deterministic还是stochastic？如何得出最优策略？

### Bellman optimality equation (BOE)

#### Introduction

Bellman optimality quation (elementwise form):
$$
\begin{aligned}v(s)&={\color{red}\max_\pi}\sum_a{\color{red}\pi(a|s)}\left(\sum_rp(r|s,a)r+\gamma\sum_{s'}p(s'|s,a)v(s')\right),\quad\forall s\in\mathcal{S}\\&={\color{red}\max_\pi}\sum_a{\color{red}\pi(a|s)}q(s,a)\quad s\in\mathcal{S}\end{aligned}
$$
Remarks:

​	$p( r| s, a) , p( s^{\prime }| s, a)$ are known.
​	$v( s) , v( s^{\prime })$ are unknown and to be calculated.
​	Is $\pi(s)$ known or unknown?  

​	==**在贝尔曼公式中策略 $\pi$ 是已知的，而在贝尔曼最优公式中策略 $\pi$ 是待求的最优策略**== 

Bellman optimality quation (matrix-vector form):
$$
v=\max_\pi(r_\pi+\gamma P_\pi v)
$$

#### Maximization on the right-hand side

==Fix $v(s')$== first and solve $\pi$ :

由于给了 $v(s')$ 一个初值将其暂时固定，则右式中的 $q(s,a)$ 可视作定值

<img src="C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250315005817508.png" alt="image-20250315005817508" style="zoom:80%;" />

这个例子中的 $c_n$ 就对应着公式中的 $\pi(a|s)$ , 因为 $\pi(a_i|s)$ 也满足==非负==和==求和为0==的条件

Inspired by the above example, considering that $\sum_a\pi(a|s)=1$, we have
$$
\max_\pi\sum_a\pi(a|s)q(s,a)={\color{red}\max_{a\in\mathcal{A}(s)}}q(s,a)
$$
where the optimality is achieved when:
$$
\pi(a|s)=\left\{\begin{array}{ll}1&a=a^*\\0&a\neq a^*\end{array}\right.
$$
where $a^*=\arg\max_aq(s,a)$

#### Rewrite as $v=f(v)$ 

We already know that the Bellman optimality quation in matrix-vector form is:
$$
v=\max_\pi(r_\pi+\gamma P_\pi v)
$$
Let:
$$
f(v) = \max_\pi(r_\pi+\gamma P_\pi v)
$$
由前文得，我们在求解最优的 $\pi$ 时需要**先给定一个初始 $v$ **, 因此 $\max_\pi(r_\pi+\gamma P_\pi v)$ 一定是一个关于 $v$ 的函数

其中 $v$ 是一个列向量，每个元素都是一个状态 $s$ 下的state value，因此 $f(v)$ 也是一个列向量

$$
[f(v)]_s=\max_\pi\sum_a\pi(a|s)q(s,a)\quad s\in\mathcal{S}
$$

#### Contraction mapping theorem

不动点 Fixed point：$x\in X$ is a fixed point of $f:X\to X$ if $f(x)=x$

收缩映射 Contraction mapping：$f$ is a contraction mapping if
$$
\|f(x_1)-f(x_2)\|\leq\gamma\|x_1-x_2\|\quad where\ \gamma\in(0,1)
$$
此处 $||·||$ 可以是任意一种向量范数

收缩映射定理 Contration mapping theorem:

​	For any equation that has the form of $x=f(x)$ ,if $f$ is a *contraction mapping* , then:

1. 存在性 Existence: there exists a fixed point $x^*$ satisfying $f(x^*)=x^*$.
2. 唯一性 Uniqueness: The fixed point $x^*$ is unique.
3. 求解算法 Algorithm: Consider a sequence $\{x_k\}$ where $x_{k+1}=f(x_k),then$ $x_k\to x^*$ as $k\to\infty.$ Moreover, the convergence rate is exponentially fast.

proof: 详见书P43

​	首先证明数列 ${x_k=f(x_{k-1})}_{k=1}^\infty$ 是柯西数列，从而得到这个数列是收敛到一个值 $x^*$ 的

​	然后证明 $x^*$ 是一个不动点

​	再证明不动点 $x^*$ 是唯一的

​	最后证明 $x_k$ 以指数级速度收敛到 $x^*$ 

#### Solution

First we have to prove the $f$ in $v=f(v)$ is a contraction function

proof: 详见书P44  此式中的 $||·||$ 应该取无穷范数 $||·||_\infty$  即**向量中元素绝对值的最大值**![image-20250317003140907](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250317003140907.png)

Applying the Contraction mapping theorem gives the following results:

<img src="C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250317003300238.png" alt="image-20250317003300238" style="zoom:80%;" />

#### Optimality

Suppose $v^*$ is the solution to the Bellman optimality equation. It satisfies
$$
v^*=\max_\pi(r_\pi+\gamma P_\pi v^*)
$$
Suppose
$$
\pi^*=\arg\max(r_{\pi}+\gamma P_{\pi}v^*)
$$
$\pi^*$ 是使得 $r_\pi+\gamma P_\pi v^*$ 最大的策略

Then
$$
v^*=r_{\pi^*}+\gamma P_{\pi^*}v^*
$$
这就是一个 $\pi^*$ 策略下的贝尔曼公式，而 $v^*=v_\pi^*$ 就是对应 $\pi^*$ 策略的state value

由此也能看出**贝尔曼最优公式就是一个特殊的贝尔曼公式**，特殊之处在于其依据的策略 $\pi^*$ 是最优策略

<img src="C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250317075610648.png" alt="image-20250317075610648" style="zoom:80%;" />

proof:



what does the optimal policy $\pi^*$ look like?

For any $s\in S$ , the ==deterministic greedy== policy
$$
\pi^*(a|s)=\left\{\begin{array}{cc}1&a=a^*(s)\\0&a\neq a^*(s)\end{array}\right.
$$
is an optimal policy solving the BOE.  最优策略即**在状态 $s$ 选择 action value最大的行动 $a^*$**
$$
a^*(s)=\arg\max_aq^*(a,s)
$$
where $q^*(a,s) =\sum_rp(r|s,a)r+\gamma\sum_{s^\prime}p(s^\prime|s,a)v^*(s^\prime)$  即在状态 $s$ 下采取行动 $a$ 的 action value

### Analyzing optimal policies

What factors determine the optimal policy?

It can be clearly seen from the BOE
$$
v(s)=\max_{\pi}\sum_{a}\pi(a|s)\left(\sum_{r}{\color{red}p(r|s,a)r}+{\color{red}\gamma}\sum_{s^{\prime}}{\color{red}p(s^{\prime}|s,a)}v(s^{\prime})\right)
$$
that there are 3 factors:

​	Reward design: $r$

​	System model: $p(s\prime |s,a)$, $p(r|s,a)$ 

​	Discount rate: $\gamma$

$v(s)$, $v(s\prime)$, $\pi(a|s)$ are unknown to be calculated

其中 System model 一般很难改变，因此下文用例子说明改变其他两个量对最优策略 $\pi^*$ 的影响

#### Change discounted rate $\gamma$

The optimal policy is more far-sighted as $\gamma$ gets bigger (closer to 1), acoordingly, it's more short-sighted as $\gamma$ gets smaller (closer to 0).  左图为求解的最优策略 右图为对应的state value

<img src="C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250318120859622.png" alt="image-20250318120859622" style="zoom:80%;" />

<img src="C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250318120916650.png" alt="image-20250318120916650" style="zoom:80%;" />

<img src="C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250318120958564.png" alt="image-20250318120958564" style="zoom:80%;" />

#### Change reward $r$ 

<img src="C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250318121432763.png" alt="image-20250318121432763" style="zoom:80%;" />

### Summary

<img src="C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250318122446980.png" alt="image-20250318122446980" style="zoom:80%;" />

<img src="C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250318122539438.png" alt="image-20250318122539438" style="zoom:80%;" />

关于唯一性：注意 ==optimal state value 是唯一的==，但 ==optimal policy 不一定是唯一的==

## Chapter-4 Value Iteration&Policy Iteration

第一次正式介绍 model-based 的强化学习算法

### Value iteration algorithm

The algorithm（注意这个式子与贝尔曼公式的区别，这说明 $v_k$ 不是 state value）
$$
v_{k+1}=\max_\pi(r_\pi+\gamma P_\pi v_k)
$$
can be decomposed to two steps:

Step 1: **policy update**. This step is to solve
$$
\pi_{k+1}=\arg\max_\pi(r_\pi+\gamma P_\pi v_k)
$$
where $v_k$ is given.  根据迭代得到的新的 $v_k$ 向量的取值计算新的使 $r_\pi+\gamma P_\pi v_k$ 最大的策略

The elementwise form:

<img src="C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250401095754554.png" alt="image-20250401095754554" style="zoom:80%;" />

Step 2: **value update**.
$$
v_{k+1}=r_{\pi_{k+1}}+\gamma P_{\pi_{k+1}}v_k
$$
$\pi_{k+1}$ 就是在给定 $v_k$ 的条件下计算出的策略，再用这个策略迭代出 $v_{k+1} $ 

注意：这里的 $v_k$ 并不是 state value, 而是从一个任意给定的 $v_0$ 开始不断迭代得到的值

​            $v_k$ 并不一定满足 Bellman equation

The elementwise form:

<img src="C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250401100110414.png" alt="image-20250401100110414" style="zoom:80%;" />

**Pseudocode**

​	Summary: $v_k(s)\to q_k(s,a)\to\text{greedy policy}\ \pi_{k+1}(a|s)\to\mathrm{new~value}\ v_{k+1}=\max_a q_k(s,a)$ 

<img src="C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250401101156331.png" alt="image-20250401101156331" style="zoom:80%;" />

### Policy iteration algorithm

#### Algorithm description

Given a random initial policy $\pi_0$ ,

Step 1: **policy evaluation (PE)**

This step is to calculate the state value of $\pi_k$:
$$
v_{\pi_k} = r_{\pi_k} + \gamma P_{\pi_k}v_{\pi_k}
$$
即根据既定的策略计算每一个状态的 state value（这里的 $v_{\pi_k}$ 都是 state value）

<img src="F:\新建文件夹\WeChat Files\wxid_ygzltfcqkee422\FileStorage\Temp\bfb0b50700574504b97fb01f1a8971a.png" alt="bfb0b50700574504b97fb01f1a8971a" style="zoom:80%;" />

Step 2: **policy immprovement (PI)**
$$
\pi_{k+1}=\arg\max_\pi(r_\pi+\gamma P_\pi v_{\pi_k})
$$
即根据 $v_{\pi_k}$ 迭代出更优的 $\pi_{k+1}$ 

The maximization is componentwise  即每个状态的最优行动是独立计算的

The elementwise form:

<img src="C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250401113329320.png" alt="image-20250401113329320" style="zoom:80%;" />

The algorithm leads to a sequence
$$
\pi_{0}\xrightarrow{PE}v_{\pi_{0}}\xrightarrow{PI}\pi_{1}\xrightarrow{PE}v_{\pi_{1}}\xrightarrow{PI}\pi_{2}\xrightarrow{PE}v_{\pi_{2}}\xrightarrow{PI}\ldots
$$
$\text{PE=policy evaluation,\ PI=policy improvement}$

**pseudocode**:

<img src="C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250401120128336.png" alt="image-20250401120128336" style="zoom:80%;" />

Q1. policy evaluation 中是如何根据 $\pi_k$ 计算 $v_{\pi_k}$ 的？

​	矩阵算法和迭代算法

​	详见CH2 Bellman equation 的 Solve state value部分

Q2. 为什么在 policy improvement 中迭代出的新策略 $\pi_{k+1}$ 一定比 $\pi_k$ 更优？

<img src="C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250401105235876.png" alt="image-20250401105235876" style="zoom:80%;" />

Here, $v_{\pi_{k+1}}\geq v_{\pi_k}$ means that $ v_{\pi_{k+1}}(s)\geq v_{\pi_k}(s)$ for all $s$ 

proof:

Since $v_{\pi_{k+1}}$ and $v_{\pi_{k}}$ are state values, they satisfy the Bellman equations:

$$
\begin{aligned}v_{\pi_{k+1}}&=r_{\pi_{k+1}}+\gamma P_{\pi_{k+1}}v_{\pi_{k+1}}\\v_{\pi_{k}}&=r_{\pi_k}+\gamma P_{\pi_k}v_{\pi_k}\end{aligned}
$$
Since $\pi_{k+1}=\arg\max_\pi(r_{\pi}+\gamma P_{\pi}|v_{\pi_{k}})$, we know that

$$
r_{\pi_{k+1}}+\gamma P_{\pi_{k+1}}v_{\pi_k}\geq r_{\pi_k}+\gamma P_{\pi_k}v_{\pi_k}.
$$
注意这里左式的 $v_{\pi_k}$ 不变是因为这是迭代式中给定的值，不是随着 PI 步骤改变的

It then follows that

$$
\begin{aligned}v_{\pi_{k}}-v_{\pi_{k+1}}&=(r_{\pi_k}+\gamma P_{\pi_k}v_{\pi_k})-(r_{\pi_{k+1}}+\gamma P_{\pi_{k+1}}v_{\pi_{k+1}})\\&\leq(r_{\pi_{k+1}}+\gamma P_{\pi_{k+1}}v_{\pi_k})-(r_{\pi_{k+1}}+\gamma P_{\pi_{k+1}}v_{\pi_{k+1}})\\&\leq\gamma P_{\pi_{k+1}}(v_{\pi_k}-v_{\pi_{k+1}}).\end{aligned}
$$
Therefore,

$$
\begin{aligned}v_{\pi_k}-v_{\pi_{k+1}}\leq\gamma^2P_{\pi_{k+1}}^2(v_{\pi_k}-v_{\pi_{k+1}})&\leq\ldots\leq\gamma^nP_{\pi_{k+1}}^n(v_{\pi_k}-v_{\pi_{k+1}})\\&\leq\lim_{n\to\infty}\gamma^nP_{\pi_{k+1}}^n(v_{\pi_k}-v_{\pi_{k+1}})=0.\end{aligned}
$$
The limit is due to the facts that $\gamma^n\to0$ as $n\to\infty$ and $P_{\pi_{k+1}}^n$ is a nonnegative stochastic matrix for any $n.$ Here, a stochastic matrix refers to a nonnegative matrix whose row sums are equal to one for all rows.

Q3. 为什么这样的迭代算法最终能得到最优策略？

Since every iteration would improve the policy,we know
$$
v_{\pi_0}\leq v_{\pi_1}\leq v_{\pi_2}\leq\cdots\leq v_{\pi_k}\leq\cdots\leq v^*.
$$
直观来看似乎 $v_{\pi_k}$ 持续增大并最终收敛，但我们仍需证明其最终收敛到 $v^*$ 

$v^*$ 是贝尔曼最优公式的解

<img src="C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250401111458848.png" alt="image-20250401111458848" style="zoom:80%;" />

proof：



Q4. policy iteration 和 value iteration 之间的关系

​	证明 policy iteration 收敛需要使用” value iteration 收敛“的结论

​	分别是**截断策略算法 Truncated policy iteration algorithm**的两个极端

#### Easy example

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\64b308bc01c75a466a6dbb3788835f1.jpg" alt="64b308bc01c75a466a6dbb3788835f1" style="zoom: 60%;" />

#### Complicated example

发现：接近target的状态的策略会先达最优，远离target的状态的策略会后达最优

### Truncated policy iteration algorithm

#### Compare policy iteration and value iteration 

The two algorithms are very similar:
$$
\text{Policy iteration:}\ \pi_0\xrightarrow{PE}v_{\pi_0}\xrightarrow{PI}\pi_1\xrightarrow{PE}v_{\pi_1}\xrightarrow{PI}\pi_2\xrightarrow{PE}v_{\pi_2}\xrightarrow{PI}\ldots\\\text{Value iteration:}\quad \quad \quad \ 
\ \ u_0\xrightarrow{PU}\pi_1^{\prime}\xrightarrow{VU}u_1\xrightarrow{PU}\pi_2^{\prime}\xrightarrow{VU}u_2\xrightarrow{PU}\ldots
$$
PE = policy evaluation  PI = policy improvement  ;  PU = policy update  VU = value update

  <img src="C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250401162735099.png" alt="image-20250401162735099" style="zoom:80%;" />

为了让两个算法具有可比性，我们强行令 $v_0 = v_{\pi_0}$ , 但其实做值迭代时初始值 $v_0$ 可以赋任意值

会发现一直到表中第3)步两个算法都完全一致

但第4)步中  policy iteration 通过迭代解贝尔曼方程求出 $v_{\pi_1}$ , 而 value iteration 直接把 $v_0$ 代入一步运算求出 $v_1$ 

此时 $v_{\pi_1}$ 与 $v_1$ 已不再相同

<img src="C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250401164825212.png" alt="image-20250401164825212" style="zoom:80%;" />

在使用迭代法解 $v_{\pi_1}=r_{\pi_1}+\gamma P_{\pi_1}v_{\pi_1}$ 时，如果把初始值也赋为 $v_0$ , 会发现第一步迭代就能得到 value iteration中要求的 $v_1$ ，而迭代无穷次后才能得到 policy iteration 中要求的 $v_{\pi_1}$ 

如果在这两个极限之间，规定一个有限的迭代次数 $j$ , 就是**截断策略迭代算法**

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\1745249634312.png" alt="1745249634312" style="zoom:80%;" />

不难发现通过截断，求解贝尔曼公式时得到的 $v_k\neq v_{\pi_k}$ , 这会导致整个算法不再收敛吗？

proof:



![image-20250401171327341](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250401171327341.png)

### Summary

<img src="C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20250401171355024.png" alt="image-20250401171355024" style="zoom:80%;" />

## Chapter-5 Monte Carlo Learning

第一次正式介绍 model-free 的强化学习算法

value iteration 和 policy iteration 方法准确来说是动态规划方法，实际上MBRL (model-based reinforcement learnig) 指的是通过大量数据估计出来一个模型，再基于这个模型进行强化学习

但本课程中将 value iteration 和 policy iteration 方法也归于MBRL

### Motivating example: Monte Carlo estimation

抛硬币，结果为随机变量 $X$ ，结果为正面时 $X=1$ ，为背面时 $X=-1$ ，目标为求 $\mathbb{E}(X)$

 #### Model-based

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\1745251074174.png" alt="1745251074174" style="zoom:80%;" />

但如此精确的模型在实际使用时很难获得

#### Model-free

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\1745251152600.png" alt="1745251152600" style="zoom:80%;" />

通过多次使用取平均来估计期望值，数学依据为大数定理：

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\1745251264676.png" alt="1745251264676" style="zoom:80%;" />

总结：所谓 Monte-Carlo estimation 就是一种==通过大量采样数据和实验结果来进行近似==的思想

### MC Basic

#### Convert policy iteration to be model-free

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\1745752128418.png" alt="1745752128418" style="zoom:80%;" />

从前面的学习我们知道，$q_{\pi_k}(s,a)$ 有两种表示方法：

表达式1需要 model 才能计算，即式中的 $p(r|s,a)$ 和 $p(s^{\prime}|s,a)$ 必须是已知的
$$
q_{\pi_{k}}(s,a)=\sum_{r}p(r|s,a)r+\gamma\sum_{s^{\prime}}p(s^{\prime}|s,a)v_{\pi_{k}}(s^{\prime})
$$
而依据 action value 最原始定义的表达式2是 model-free 的，我们可以==**依据数据来计算/估计 $q_{\pi_k}(s,a)$ **==
$$
q_{\pi_k}(s,a)=\mathbb{E}[G_t|S_t=s,A_t=a]
$$
使用 Monte Carlo 方法估计 action values 的流程：

1. Starting from $(s,a)$, following policy $\pi_k$, generate an episode.

2. The discounted return of this episode is $g(s,a)$

3. $g(s,a)$ is a sample of $G_t$ in $q_{\pi_k}(s,a) = \mathbb{E}[G_t|S_t = s, A_t = a]$

4. Suppose we have a set of episodes and hence $\{g^{(j)}(s,a)\}$​. Then, 
   $$
   q_{\pi_k}(s,a) = \mathbb{E}[G_t|S_t = s, A_t = a] \approx \frac{1}{N} \sum_{i=1}^{N} g^{(i)}(s,a)
   $$

==***核心思想：当没有模型的时候，我们要有足够多的数据***==

#### The MC Basic algorithm

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\1745753603715.png" alt="1745753603715" style="zoom:80%;" />

与 model-based policy iteration 算法的唯一区别在于 step1 中直接通过数据估计 $q_{\pi_k}$ 而非求解 $v_{\pi_k}(s)$ 

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250427193637237.png" alt="image-20250427193637237" style="zoom:80%;" />

​	MC Basic 揭示了 MC-based model-free RL 的核心思想，但由于**计算效率过低并不实用**

​	由于 policy iteration 是收敛的，在有足够多数据前提下的 MC Basic 也是可以保证收敛的；但以后**随着算法越来越复杂，它们不再一定具有收敛性**

#### Illusion example: Episode length

 Episode length 指的是“探索的长度”，即计算 $g(s,a)$ 时往后计算几项

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250427195340980.png" alt="image-20250427195340980" style="zoom:80%;" />

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250427195712748.png" alt="image-20250427195712748" style="zoom:80%;" />

发现：

1. 当 episode length 比较小的时候，只有离目标比较近的状态能够“抵达目标”，体现为 state value 是正数
2. 随着 episode length 逐渐增大，离目标较远的 state 也渐渐可以在**“行动次数被限制”**的探索过程中抵达目标
3. 观察上面8张图，尤其是后4张可以知道 episode length 必须要足够长，但也不需要无限长

### Use data more efficiently: MC Exploring Starts

#### Utilizing samples more efficiently

假设我们根据给定的策略 $\pi$ 获得了***一个*** episode 
$$
s_1\xrightarrow{a_2}s_2\xrightarrow{a_4}s_1\xrightarrow{a_2}s_2\xrightarrow{a_3}s_5\xrightarrow{a_1}\ldots
$$
注意这里状态和行动的下标都不再是时间步长，而是索引编号

每当一个 *state-action pair* 出现在 episode 中一次，就称为对其的一次 *visit*

**Initial-visit strategy**: 一整个 episode 只用于估计初始  *state-action pair* 的 action value ，这也正是 MC-Basic 方法中使用的，显然没有充分利用数据
$$
\begin{aligned}s_{1}\xrightarrow{a_{2}}s_{2}\xrightarrow{a_{4}}s_{1}\xrightarrow{a_{2}}s_{2}\xrightarrow{a_{3}}s_{5}\xrightarrow{a_{1}}&\ldots\quad\mathrm{[original~episode]}\\s_{2}\xrightarrow{a_{4}}s_{1}\xrightarrow{a_{2}}s_{2}\xrightarrow{a_{3}}s_{5}\xrightarrow{a_{1}}&\ldots\quad[\text{subepisode starting from }(s_{2},a_{4})]\\s_{1}\xrightarrow{a_{2}}s_{2}\xrightarrow{a_{3}}s_{5}\xrightarrow{a_{1}}&\ldots\quad[\text{subepisode starting from }(s_{1},a_{2})]\\s_{2}\xrightarrow{a_{3}}s_{5}\xrightarrow{a_{1}}&\begin{array}{cc}\ldots&\ [\text{subepisode starting from }(s_{2},a_{3})]\end{array}\\s_{5}\xrightarrow{a_{1}}&\begin{array}{cc}\ldots&\ [\text{subepisode starting from }(s_5,a_1)]\end{array}\end{aligned}
$$
每一个 subepisode 都可以视作一个从不同的 *state-action pair* 出发的新 episode，从而一个 episode 就可以用于估计很多 *state-action pair* 的 action value

在一个 episode 中同一个 *state-action pair* 可能会出现很多次，只在第一次出现时计算就是 **First-visit strategy** ，每次都计算就是 **Every-visit strategy**

#### Updating polocies more efficiently

The first strategy is, in the policy evaluation step, to **collect all the episodes starting from the same state-action pair and then approximate the action value using the *average return of these episodes*.** This strategy is adopted in the MC Basic algorithm. ==在获取并计算了大量 episode 的 diacounted return 之后才估计 action value==

The second strategy, which can overcome this drawback, is to **use the *return of a* *single episode* to approximate the corresponding action value.** In this way, we can immediately obtain a rough estimate when we receive an episode. Then, the policy can be improved in an episode-by-episode fashion. ==每计算完一个 episode 的 discounted return 就用来粗略估计 action value，并对该状态下的策略进行更新==

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250509103312125.png" alt="image-20250509103312125" style="zoom:80%;" />

MC Exploring Starts 算法需要==从每一个 *state-action pair* **出发的**==足够多的 episode

比如我需要很多 $(s_3,a_7)$ 的数据来估计其 action value，实际上如果我从其他的 $(s,a)$ 出发如果经过了 $(s_3,a_7)$ 也是可以获得一个 episode 来更新策略的，但是这并没有被保证，所以只有从 $(s_3,a_7)$  出发的 episode 才是保证一定能获得我们需要的数据的

### MC without exploring starts: MC $\epsilon$-Greedy

#### Soft policies

当一个 policy ==**在每个状态采取所有行动的可能性都为正数**==时，称之为 soft policy，这是 stochastic policy 的一种

引入 soft policy 后，我们==只需要少量足够长的 episode，就能保证每个 *state-action pair* 都被 visit 足够多次==，而不需要从每一个 *state-action pair* **出发的**很多 episode

#### $\epsilon$-greedy policies

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250509104952124.png" alt="image-20250509104952124" style="zoom:80%;" />

选择 greedy action 的概率永远比其他 action 高，因为 $1-\frac{\varepsilon}{|\mathcal{A}(s)|}(|\mathcal{A}(s)|-1)=1-\varepsilon+\frac{\varepsilon}{|\mathcal{A}(s)|}\geq\frac{\varepsilon}{|\mathcal{A}(s)|}$

使用 $\epsilon$-greedy 实际上就是在 exploitation(greedy) 和 expolration 中进行平衡，即“是完全相信目前获取的 action value 并进行最贪婪的策略更新，还是持怀疑态度，给目前来看 action value 不是最大的行动也留一些探索概率”

​	当 $\epsilon=0$ 时，就退化成纯粹的 greedy

​	当 $\epsilon=1$ 时，退化成**均匀分布**，探索性更强

#### MC $\epsilon$-Greedy algorithm

调整之前算法的 policy improvement 步骤

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250509110043785.png" alt="image-20250509110043785" style="zoom:80%;" />

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250509110521677.png" alt="image-20250509110521677" style="zoom:80%;" />

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250509110912222.png" alt="image-20250509110912222" style="zoom:80%;" />

#### Example: Exploration ability

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250509111643636.png" alt="image-20250509111643636" style="zoom:80%;" />

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250509112007231.png" alt="image-20250509112007231" style="zoom:80%;" />

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250509112554277.png" alt="image-20250509112554277" style="zoom:80%;" />

优点：探索性强，因此不再需要“exploration starts”条件

缺点：没有最优性，可以通过设置 $\epsilon$ 逐渐减小来一定程度上弥补这一点

### Summary

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250509113437692.png" alt="image-20250509113437692" style="zoom:80%;" />

## Chapter-6 Stochastic Approximation and Stochastic Gradient Descent

随机近似理论与随机梯度下降

### Motivating example: Mean estimation

non-incremental method: $\mathbb{E}[X]\approx\bar{x}\doteq\frac{1}{n}\sum_{i=1}^nx_i$  非增量，要等待获取全部数据才能计算

incremental method:  增量/迭代方式  每接收到一个sample就可以立即计算均值  随着数据量增长越来越逼近真实期望值
$$
w_{k+1}\doteq\frac{1}{k}\sum_{i=1}^{k}x_{i},\quad k=1,2,\ldots\\
w_k=\frac{1}{k-1}\sum_{i=1}^{k-1}x_i,\quad k=2,3,\ldots\\
w_{k+1}=\frac{1}{k}\sum_{i=1}^kx_i=\frac{1}{k}\left(\sum_{i=1}^{k-1}x_i+x_k\right)=\frac{1}{k}((k-1)w_k+x_k)=w_k-\frac{1}{k}(w_k-x_k)
$$
用 $\alpha_k>0$ 替代系数 $\frac{1}{k}$ 得到更 general 的表达式：
$$
w_{k+1}=w_k-\alpha_k(w_k-x_k)
$$
后面的学习将会证明：

1. 在 $\alpha_k$ 满足某些简单的条件时，该算法依然可以在 $k\to\infty$ 时收敛到 $\mathbb{E}[X]$ 
2. 这个算法是一个特殊的 Stochastic Approximation 算法，也是一个特殊的 Stochastic Gradient Descent 算法
3. 下一章中 Temporal-Difference 算法也有相似但更复杂的表达形式

### Robbins-Monro algorithm

Stochasitc approximation 指代的是一大类**用于求解方程或优化问题**的**随机迭代(stochastic iterative)算法**，RM是其中之一

与其他求解方程的算法相比，其优势为==**不需要知道目标方程或其导数的表达式**==

#### Problem statement

假设我们要求解方程 $g(w)=0$ 的根，其中 $w\in\mathbb{R}$ 是未知变量，$g:\mathbb{R}\to \mathbb{R}$ 是一个函数

许多问题最终都能转化为这样一个求解方程的问题，比如优化目标函数 $J(w)$ 可以转化为 $g(w)\doteq\nabla_wJ(w)=0$  

当 $g$ 的表达式或其导数已知时，有很多种数值方法求解此问题

但当 $g$ 的表达式未知，比如说是由一个结构和参数未知的神经网络表示的，或者说只能观测到有噪声的 $g(w):\tilde{g}(w,\eta)=g(w)+\eta$ , 此时整体就像一个黑箱系统，我们要==仅利用输入 $w$ 和输出 $\tilde{g}(w,\eta)$ 来求解 $g(w)=0$==

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250510094343706.png" alt="image-20250510094343706" style="zoom:80%;" />

#### Algorithm description

可以利用 Robbins-Monro 算法解决这个问题：
$$
\color{red}w_{k+1}=w_k-a_k\tilde{g}(w_k,\eta_k),\quad k=1,2,3,\ldots
$$
其中 $w_k$ 是对于解的第 $k$ 次估计，$\tilde{g}(w_k,\eta_k)=g(w_k)+\eta_k$ 是第 $k$ 次有噪声的观测，$a_k$ 是个**正**参数

运作方式为：先初始化一个 $w_1$ 输入黑盒得到输出 $\tilde{g}(w_1,\eta_1)$ , 然后代入上式迭代出 $w_2$ , 再把 $w_2$ 输入黑盒得到 $\tilde{g}(w_2,\eta_2)$ , 再接着迭代......

#### Convergence analysis

为什么经过RM算法迭代最终可以收敛到方程 $g(w)=0$ 的解？

先看一个简单例子：

​	$g(w)=\tanh(w-1)$   Parametres: $w_1=3$, $a_k=\frac{1}{k}$, $\eta_k\equiv0$ for simplicity

​	方程 $g(w)=0$ 的真实解为 $w^*=1$

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250510114913986.png" alt="image-20250510114913986" style="zoom:80%;" />

​	上图为仿真结果，可以直观发现 $w_{k+1}$ 比 $w_k$ 更接近 $w^*$，最终收敛到真实解 $w^*=1$

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250510115126310.png" alt="image-20250510115126310" style="zoom:80%;" />

下面进行严谨的数学证明：

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250510120942214.png" alt="image-20250510120942214" style="zoom:80%;" />

条件①：函数 $g$ 单调递增，这保证方程 $g(w)=0$ 存在唯一解；$g$ 的梯度有上界

条件②：$\sum_{k=1}^{\infty}a_{k}^{2}<\infty$ 确保 $a_k$ 收敛到0，而 $\sum_{k=1}^\infty a_k=\infty$ 确保 $a_k$ 不要太快收敛到0

​		满足这一条件的常见序列 —— $a_k=\frac{1}{k}$ , $a_k=\frac{1}{k+1}$ , $a_k=\frac{c_k}{k}$ where $c_k$ is bounded

条件③：$\eta$ 的期望为0，方差有界；不要求 $\eta$  是高斯分布的；一种特殊而常见的情况是 $\{\eta_k\}$ 是一个独立同分布的随机变量序列

以上三个条件是满足“**从任意初始值出发**都可以用RM算法迭代解出方程的解”的前提

有的 $g$ 不满足条件①，但在特定的初始值下也能收敛到方程的解；RM算法中常把 $a_k$ 设为一个足够小的常数，这并不满足条件②，但算法在某种意义上仍能有效工作

*其实这里还是没有证明 RM 算法为什么收敛，这需要先证明一个更复杂的定理 Dvoretzky‘s Theorem，详见书P110* 

#### Apply to mean estimation

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250510135131123.png" alt="image-20250510135131123" style="zoom:80%;" />

通过证明这个 mean estimation algorithm 是 RM algorithm 的一个特例，就可以证明当 $\alpha_k$ 不等于 $\frac{1}{k}$ 的时候 $w_{k+1}\to \mathbb{E}[X]$ 仍然是成立的

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250510140532887.png" alt="image-20250510140532887" style="zoom:80%;" />

### Stochastic Gradient Descent

SGD算法是RM算法的一个特殊情况

#### Algorithm description

考虑一个问题，目标是解决下述优化问题：
$$
\min_wJ(w)=\mathbb{E}[f(w,X)]
$$
其中 $w$ 是要优化的参数；$X$ 是随机变量，期望就是针对 $X$ 

三种解决方法：

 1. Gradient Descent（GD）
    $$
    w_{k+1}=w_k-\alpha_k\nabla_w\mathbb{E}[f(w_k,X)]=w_k-\alpha_k\mathbb{E}[\nabla_wf(w_k,X)]
    $$
    沿着梯度方向下降，从而找到最小值；其中 $\alpha_k$ 是步长，决定了下降的快慢；期望运算和梯度运算可交换

    缺点：当 $X$ 的概率分布模型未知时，梯度期望值很难获取

 2. Batch Gradient Descent（BGD）
    $$
    \mathbb{E}[\nabla_{w}f(w_{k},X)]\approx\frac{1}{n}\sum_{i=1}^{n}\nabla_{w}f(w_{k},x_{i})\\w_{k+1}=w_k-\alpha_k\frac{1}{n}\sum_{i=1}^n\nabla_wf(w_k,x_i)
    $$
    没有模型 → 用数据来估计期望

    缺点：每次迭代计算下一个 $w_k$ 都需要大量的数据

 3. Stochastic Gradient Descent（SGD）

    $$
    w_{k+1}=w_k-\alpha_k\nabla_wf(w_k,\color{red}x_k\color{black})
    $$
    与 GD 相比，用随机采样 $x_k$ 替代了变量 $X$ ，即用**随机梯度** $\nabla_wf(w_k,x_k)$ 替代了真实梯度 $\nabla_w\mathbb{E}[f(w_k,X)]$ ；与 BGD 相比，就是把 batch 的容量 $n$ 定为1

#### Application to mean estimation

通过将 mean estimation 问题构造为一个优化问题：
$$
\min_wJ(w)=\mathbb{E}\left[\frac{1}{2}\|w-X\|^2\right]\doteq\mathbb{E}[f(w,X)]
$$
我们可以证明 ==**mean estimation 算法也是一种特殊的 SGD 算法**==

用 SGD 解决上述优化问题：
$$
\begin{aligned}
&g(w)=\nabla_w\mathbb{E}[f(w,X)],\ \tilde{g}(w_k,\eta_k)=\nabla_wf(w,x_k)\\
&w_{k+1}=w_k-\alpha_k\nabla_wf(w_k,x_k)=w_k-\alpha_k\nabla_w\left(\frac{1}{2}\|w_k-x_k\|^2\right)=w_k-\alpha_k(w_k-x_k)
\end{aligned}
$$
发现形式与增量形式的 mean estimation 算法完全一致，因此证明其为**用于解决期望问题**的一种特殊 SGD 算法

#### Convergence analysis

欲证 SGD 收敛，仅需证明==**SGD 是一种特殊的 Robbins-Monro 算法**==，也能由此获得 SGD 的收敛条件

SGD 的目标是最小化 $J(w)=\mathbb{E}[f(w,X)]$ ，这可以转化为一个求解方程的问题：
$$
\nabla_wJ(w)=\mathbb{E}[\nabla_wf(w,X)]=0
$$
令 $g(w)=\nabla_wJ(w)=\mathbb{E}[\nabla_wf(w,X)]$ ，问题就转化为了寻找方程 $g(w)=0$ 的根

用 RM 算法来求解这个问题：
$$
\begin{aligned}\tilde{g}(w,\eta)&=\nabla_wf(w,x)\\&=\underbrace{\mathbb{E}[\nabla_wf(w,X)]}_{g(w)}+\underbrace{\nabla_wf(w,x)-\mathbb{E}[\nabla_wf(w,X)]}_{\eta}\end{aligned}
$$
测量值  $\tilde{g}(w,\eta)$ 在这里就是随机梯度，而噪音就是随机梯度与真实梯度的差

RM算法：$w_{k+1}=w_{k}-a_{k}\tilde{g}(w_{k},\eta_{k})=w_{k}-a_{k}\nabla_{w}f(w_{k},x_{k})$  发现恰好就是 SGD 算法的表达式

因此 SGD 就是**解决优化（最小化/最大化）形如 $J(w)=\mathbb{E}[f(w,X)]$ 一类函数的问题**的特殊RM 算法

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250511120410636.png" alt="image-20250511120410636" style="zoom:80%;" />

与 RM 算法收敛条件一一对应可以得到以上三个 SGD 算法收敛的条件

#### Convergence pattern

考虑一个问题：既然 SGD 引入了随机梯度，这会不会导致其收敛到解 $w^*$ 的过程也很随机？比如一开始向反方向迭代，然后绕一大圈最终逼近 $w^*$ ?

结论为：不会， ==**SGD 在离 $w_k$ 距离 $w^*$ 很远时的行为与 GD 极其类似，只有在很靠近 $w^*$ 时行为随机性才增强**==

证明这一结论需要引入 **SGD 和 GD 的相对误差**：
$$
\delta_k\doteq\frac{|\nabla_wf(w_k,x_k)-\mathbb{E}[\nabla_wf(w_k,X)]|}{|\mathbb{E}[\nabla_wf(w_k,X)]|}
$$
分子为随机梯度与真实梯度之差，分母为真实梯度

由于当 $w_k=w^*$ 时梯度为0，即 $\mathbb{E}[\nabla_wf(w^*,X)]=0$，所以相对误差定义式可化为：
$$
\delta_{k}=\frac{|\nabla_{w}f(w_{k},x_{k})-\mathbb{E}[\nabla_{w}f(w_{k},X)]|}{|\mathbb{E}[\nabla_{w}f(w_{k},X)]-\mathbb{E}[\nabla_{w}f(w^{*},X)]|}=\frac{|\nabla_{w}f(w_{k},x_{k})-\mathbb{E}[\nabla_{w}f(w_{k},X)]|}{|\mathbb{E}[\nabla_{w}^{2}f(\tilde{w}_{k},X)(w_{k}-w^{*})]|}
$$
其中第二个等号分母的变换是运用了拉格朗日中值定理，$\tilde w_k\in[w_k,w^*]$

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250511133821031.png" alt="image-20250511133821031" style="zoom:80%;" />

根据收敛条件有 $f$ 严格凸，即对于任意 $w, X$ 有 $\nabla^2_wf \geq c>0$ 

故相对误差的分母可以化为：
$$
\begin{aligned}\left|\mathbb{E}[\nabla_{w}^{2}f(\tilde{w}_{k},X)(w_{k}-w^{*})]\right|&=\left|\mathbb{E}[\nabla_{w}^{2}f(\tilde{w}_{k},X)](w_{k}-w^{*})\right|\\&=\left|\mathbb{E}[\nabla_{w}^{2}f(\tilde{w}_{k},X)]\right|\left|(w_{k}-w^{*})\right|\geq c|w_{k}-w^{*}|\end{aligned}
$$
第一个等号是因为 $w_k-w^*$ 为常数，将上式整体替换到相对误差表达式中得到：
$$
\delta_k\leq\frac{\mid\overbrace{\nabla_wf(w_k,x_k)}^\text{stochastic gradient}-\overbrace{\mathbb{E}[\nabla_wf(w_k,X)]}^\text{true gradient}\mid}{\underbrace{c|w_k-w^*|}_{\text{distance to the optimal solution}}}
$$
这表明：1. 相对误差 $\delta_k$ 与 $|w_k-w^*|$ 成反比例关系；2. 当 $|w_k-w^*|$ 很大的时候，$\delta_k$ 很小，SGD 的行为和 GD 很相似，快速向 $w^*$ 收敛；3. 当 $|w_k-w^*|$ 很小，即 $w_k$ 距离 $w^*$ 很近的时候，收敛会呈现较大随机性

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250512074949377.png" alt="image-20250512074949377" style="zoom:80%;" />

#### A deterministic formulation

考虑优化问题：
$$
\min_w\quad J(w)=\frac{1}{n}\sum_{i=1}^nf(w,x_i)
$$
其中 $\{x_i\}_{i=1}^n$ 是一个实数集，$x_i$ 并不是任何随机变量的采样；可以发现这个问题中**不涉及任何的随机变量或期望**

解决此问题的 SD 算法为：
$$
w_{k+1}=w_k-\alpha_k\nabla_wJ(w_k)=w_k-\alpha_k\frac{1}{n}\sum_{i=1}^n\nabla_wf(w_k,x_i)
$$
假设这个实数集非常大，我们每次只能获取单个数据，由此我们得到以下迭代算法：
$$
w_{k+1}=w_k-\alpha_k\nabla_wf(w_k,x_k)
$$
这个算法看起来和 SGD 算法一模一样，但 $x_k$ 并不是某个随机变量的取样，那到底是不是 SGD 呢？以及每次获取单个数据是按照什么分布拿呢？随机吗？

为解决以上问题，我们引入随机变量 $X$，$X$ 是依据 $\{x_i\}_{i=1}^n$ 定义的，假设其概率分布为 $p(X=x_i)=1/n$

这样原问题就转化为了随机形式：
$$
\min_w\quad J(w)=\frac{1}{n}\sum_{i=1}^nf(w,x_i)=\mathbb{E}[f(w,X)]
$$
因此前面给出的算法是一个 SGD 算法，并且根据前面学的 SGD 收敛条件，从 $\{x_i\}_{i=1}^n$ 中取出的 $x_k$ 必须是独立同分布（在这里只能是独立均匀分布），所以数据是随机取出的，同一个数据可能被反复抽到

#### Summary

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250512235450421.png" alt="image-20250512235450421" style="zoom:80%;" />

## Chapter-7 Temporal-Difference Learning

### Motivating Example

考虑一个问题，解方程：
$$
w=\mathbb{E}[R+\gamma v(X)]
$$
其中 $R$ 和 $X$ 都是随机变量，假设我们可以获得 $X$ 和 $R$ 的样本序列 $\{x\}$ 和 $\{r\}$，按之前所学进行以下构造：
$$
\begin{aligned}g(w)&=w-\mathbb{E}[R+\gamma v(X)],\\\tilde{g}(w,\eta)&=w-[r+\gamma v(x)]\\&=(w-\mathbb{E}[R+\gamma v(X)])+(\mathbb{E}[R+\gamma v(X)]-[r+\gamma v(x)])\\&\doteq g(w)+\eta\end{aligned}
$$
然后就可以用 RM 算法解方程 $g(w)=0$ 的根：
$$
w_{k+1}=w_k-\alpha_k\tilde{g}(w_k,\eta_k)=w_k-\alpha_k[w_k-(r_k+\gamma v(x_k))]
$$

### TD Learning of state values

*使用 TD 算法求解一个已知策略的 state value*

#### Algorithm description

首先由已知策略获取数据（data/experience） $(s_0,r_1,s_1,\ldots,s_t,r_{t+1},s_{t+1},\ldots)\mathrm{~or~}\{(s_t,r_{t+1},s_{t+1})\}_t$

给出 TD 算法为：
$$
\begin{aligned}&v_{t+1}(s_t)=v_t(s_t)-\alpha_t(s_t)\color{red}\left[v_t(s_t)-[r_{t+1}+\gamma v_t(s_{t+1})]\right]\color{black},&&\mathrm{(7.1)}\\&v_{t+1}(s)=v_t(s),\quad\forall s\neq s_t,&&\mathrm{(7.2)}\end{aligned}
$$
其中 $s_t$ 是 $t$ 时刻智能体所处的状态， $v_t(s_t)$ 是对于该状态的 state value $v_\pi(s_t)$ 的估计，这里 TD 算法的目的就是通过迭代使对于各个状态 state value 值的估计越来越准确；$\alpha_t(s_t)$ 是 $t$ 时刻 $s_t$ 的***学习率***

(7.2)式的含义是，在 $t$ 时刻只有 $s_t$ 的 state value 估计值会改变，其他状态的 state value 估计值不变

(7.1)式中 $v_{t+1}(s_t)$ 是 new estimate，$v_t(s_t)$ 是 current estimate；

==**TD 算法可以视作一种用于解贝尔曼方程的特殊 RM 算法**==，下面使用 RM 算法解贝尔曼方程从而导出 TD 算法：

首先要换一种形式来表示 state value
$$
v_\pi(s)=\mathbb{E}\left[R_{t+1}+\gamma G_{t+1}|S_t=s\right],\quad s\in\mathcal{S}.&&\mathrm{(7.3)}\\v_\pi(s)=\mathbb{E}\left[R_{t+1}+\gamma v_\pi(S_{t+1})|S_t=s\right],\quad s\in\mathcal{S}.&&\mathrm{(7.4)}
$$
式(7.3)为常见的表示方式，其与式(7.4)等价，因为
$$
\mathbb{E}[G_{t+1}|S_{t}=s]=\sum_{a}\pi(a|s)\sum_{s^{\prime}}p(s^{\prime}|s,a)v_{\pi}(s^{\prime})=\mathbb{E}[v_{\pi}(S_{t+1})|S_{t}=s]
$$
下面将 RM 算法用于式(7.4)

定义方程  $g(v_\pi(s_t))\doteq v_\pi(s_t)-\mathbb{E}\left[R_{t+1}+\gamma v_\pi(S_{t+1})|S_t=s_t\right]$ ，那么式(7.4)就等价于 $g(v_\pi(s_t))=0$

$r_{t+1},s_{t+1}$ 分别是我们可以获取到的随机变量 $R_{t+1},S_{t+1}$ 的样本值，因此有噪声的观测值 $\tilde{g}(v_\pi(s_t))$ 定义为：
$$
\begin{aligned}\tilde{g}(v_\pi(s_t))&=v_{\pi}(s_{t})-\begin{bmatrix}r_{t+1}+\gamma v_{\pi}(s_{t+1})\end{bmatrix}\\&=\underbrace{\left(v_{\pi}(s_{t})-\mathbb{E}\left[R_{t+1}+\gamma v_{\pi}(S_{t+1})|S_{t}=s_{t}\right]\right)}_{g(v_{\pi}(s_{t}))}\\&+\underbrace{\left(\mathbb{E}\left[R_{t+1}+\gamma v_{\pi}(S_{t+1})|S_{t}=s_{t}\right]-\left[r_{t+1}+\gamma v_{\pi}(s_{t+1})\right]\right)}_{\eta}\end{aligned}
$$
从而得到解决此问题的 RM 算法：
$$
\begin{aligned}v_{t+1}(s_{t})&=v_{t}(s_{t})-\alpha_{t}(s_{t})\tilde{g}(v_{t}(s_{t}))\\&=v_t(s_t)-\alpha_t(s_t)\left[v_t(s_t)-\left(r_{t+1}+\gamma v_\pi(s_{t+1})\right)\right]\end{aligned}
$$
其中 **$v_t(s_t)$ 是在 $t$ 时刻/第 $t$ 次对 $v_\pi(s_t)$ 的估计** 

这与前面给出的 TD 算法已经非常相似，除了这里的右式包含 $v_\pi(s_{t+1})$ 项，而 TD 算法中是 $v_t(s_{t+1})$ 项

这是因为这里假设其他状态的 state value 都已知，算法仅仅是为了估计 $v_\pi(s_t)$ ；如果要估计所有状态，则用 $v_t(s_{t+1})$ 替代 $v_\pi(s_{t+1})$ 即可

但这样替代之后还能保证算法收敛吗？这个问题将会在后面 Convergence analysis 部分讨论

#### Property analysis

定义 ==**TD target  $\bar{v}_t\doteq r_{t+1}+\gamma v_t(s_{t+1})$ **==，定义 ==**TD error  $\delta_t\doteq v_t(s_t)-[r_{t+1}+\gamma v_t(s_{t+1})]=v_t(s_t)-\bar{v}_t$**==

**为什么 $\bar{v_t}$ 被称为 TD target ？**因为以上算法会使 $v(s_t)$ 随着迭代越来越接近 $\bar{v_t}$ ：
$$
\begin{aligned}&\quad \ \ v_{t+1}(s_{t})=v_{t}(s_{t})-\alpha_{t}(s_{t})\left[v_{t}(s_{t})-\bar{v}_{t}\right]\\&\Rightarrow v_{t+1}(s_{t})-\bar{v}_{t}=v_{t}(s_{t})-\bar{v}_{t}-\alpha_{t}(s_{t})\left[v_{t}(s_{t})-\bar{v}_{t}\right]\\&\Rightarrow v_{t+1}(s_{t})-\bar{v}_{t}=[1-\alpha_{t}(s_{t})][v_{t}(s_{t})-\bar{v}_{t}]\\&\Rightarrow|v_{t+1}(s_{t})-\bar{v}_{t}|=|1-\alpha_{t}(s_{t})||v_{t}(s_{t})-\bar{v}_{t}|\end{aligned}
$$
由于 $0<\alpha_t(s_t)<1$，所以 $|v_{t+1}(s_t)-\bar{v}_t|\leq|v_t(s_t)-\bar{v}_t|$，即随着 $t$ 增大，$v(s_t)$ 越来越靠近 $\bar{v_t} $ 

**如何理解 TD error 的含义？**

首先 $\delta_t$ 体现了两时间步长之间的差异

当估计准确，即 $v_t=v_\pi$ 时，TD error 的期望值为0：
$$
\begin{aligned}\mathbb{E}[\delta_{t}|S_{t}=s_{t}]&=\mathbb{E}\left[v_{\pi}(S_{t})-(R_{t+1}+\gamma v_{\pi}(S_{t+1}))|S_{t}=s_{t}\right]\\&=v_{\pi}(s_{t})-\mathbb{E}\left[R_{t+1}+\gamma v_{\pi}(S_{t+1})|S_{t}=s_{t}\right]\\&=0\end{aligned}
$$
最后一步等于0的原因与式(7.3)与式(7.4)等价的原因一致，因此 $\delta_t$ 更**体现了估计值 $v_t$ 与真实值 $v_\pi$ 之间的差异**

TD 算法与 Monte-Carlo 算法的对比：（二者都是 model-free 的算法）

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250514223900402.png" alt="image-20250514223900402" style="zoom:80%;" />

#### Convergence analysis

![image-20250514224848710](F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250514224848710.png)

由 TD 算法的形式不难发现，在 $t$ 时刻，只有当状态 $s$ 正在被访问时有 $\alpha_t(s)>0$，否则 $\alpha_t(s)=0$

所以只有当状态 $s$ 被拜访无数多次/足够多次，才能满足条件 $\Sigma_t\alpha_t(s)=\infty$  

实践中一般把 $\alpha_t$ 设置为一个小的正常数，尽管这不满足条件 $\Sigma_t\alpha_t^2(s)<\infty$ ，但有相关工作证明了这样算法也同样能收敛到真实的 $v_\pi(s)$ 

*具体证明太复杂了......*

### TD learning of action values: Sarsa

*直接预测给定策略 $\pi$ 的 action value*

#### Algorithm

首先由已知策略得到一些 experience $\{(s_t,a_t,r_{t+1},s_{t+1},a_{t+1})\}_t$

 用 state-action pair 替代前一节 TD 算法中的 state 容易得到 Sarsa 算法：
$$
\begin{aligned}q_{t+1}(s_{t},a_{t})&=q_{t}(s_{t},a_{t})-\alpha_{t}(s_{t},a_{t})\left[q_{t}(s_{t},a_{t})-(r_{t+1}+\gamma q_{t}(s_{t+1},a_{t+1}))\right],\\q_{t+1}(s,a)&=q_{t}(s,a),\quad\text{for all }(s,a)\neq(s_{t},a_{t}),\end{aligned}
$$
其中 ==**$q_t(s_t,a_t)$ 是在时刻 $t$ 对于 $q(s_t,a_t)$ 的估计**==

Sarsa 算法其实也是一个**解以下贝尔曼方程的RM算法**：
$$
q_{\pi}(s,a)=\mathbb{E}\left[R+\gamma q_{\pi}(S^{\prime},A^{\prime})|s,a\right],\quad\forall s,a.
$$
这是 action value 形式贝尔曼方程的等价式，具体证明参见书P134

收敛性：

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250514234956107.png" alt="image-20250514234956107" style="zoom:80%;" />

#### Implementation - Optimal policy learning via Sarsa

前面给出的 Sarsa 算法其实就是在做 policy evaluation，还要结合 policy improvement 才能得到最优策略

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250514235913816.png" alt="image-20250514235913816" style="zoom:80%;" />

注意在 policy improvement 中使用的是 $\epsilon$-Greedy 算法

#### Examples

现在有这样一个任务：从特定起始状态出发，找到一条到达目标状态的可行路径/策略（注意与以前网格世界例子的区别，以前是要计算出每个 state 的最优 policy）

是不是需要更多的episode才能做到算出每个state的最优policy？

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250515001346222.png" alt="image-20250515001346222" style="zoom:80%;" />

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250515001641848.png" alt="image-20250515001641848" style="zoom:80%;" />

#### Expected Sarsa

$$
\begin{aligned}q_{t+1}(s_t,a_t)&=q_t(s_t,a_t)-\alpha_t(s_t,a_t)\left[q_t(s_t,a_t)-(r_{t+1}+\gamma\color{red}\mathbb{E}[q_t(s_{t+1},A)]\color)\right],\\q_{t+1}(s,a)&=q_t(s,a),\quad\forall(s,a)\neq(s_t,a_t),\end{aligned}
$$

其中  $\mathbb{E}[q_t(s_{t+1},A)]=\sum_a\pi_t(a|s_{t+1})q_t(s_{t+1},a)\doteq \color{red}v_t(s_{t+1})$ 

与 Sarsa 相比，Expected Sarsa 的 TD target 从 $r_{t+1}+\gamma q_{t}(s_{t+1},a_{t+1})$ 变成了 $r_{t+1}+\gamma\mathbb{E}[q_t(s_{t+1},A)]$ 

显然**计算量是增大的**，但是由于不再需要对 $A_{t+1}$ 采样得到 $a_{t+1}$ ，随机变量减少可以使**算法随机性减小**

Expected Sarsa 算法在数学上是一个解以下方程的RM算法：
$$
q_{\pi}(s,a)=\mathbb{E}\left[R_{t+1}+\gamma\mathbb{E}[q_{\pi}(S_{t+1},A_{t+1})|S_{t+1}]|S_{t}=s,A_{t}=a\right],\quad\text{for all }s,a.\quad \mathrm{(7.5)}
$$
而上式是贝尔曼方程的另一种形式，把
$$
\mathbb{E}[q_{\pi}(S_{t+1},A_{t+1})|S_{t+1}]=\sum_{A^{\prime}}q_{\pi}(S_{t+1},A^{\prime})\pi(A^{\prime}|S_{t+1})=v_{\pi}(S_{t+1})
$$
代入式(7.5)就能得到：
$$
q_\pi(s,a)=\mathbb{E}\left[R_{t+1}+\gamma v_\pi(S_{t+1})|S_t=s,A_t=a\right]
$$
所以 **Expected Sarsa 也是一个解贝尔曼方程的RM算法**

#### n-step Sarsa

*包含了 Sarsa 和 Monte Carlo 两种方法*

回顾一下 action value 的定义：$q_\pi(s,a)=\mathbb{E}[G_t|S_t=s,A_t=a]$ 

其中 $G_t$ 的表示形式有很多，这也是区别不同算法的关键所在：
$$
\begin{aligned}\mathsf{Sarsa}\longleftarrow&G_{t}^{(1)}=R_{t+1}+\gamma q_{\pi}(S_{t+1},A_{t+1}),\\&G_{t}^{(2)}=R_{t+1}+\gamma R_{t+2}+\gamma^{2}q_{\pi}(S_{t+2},A_{t+2}),\\&\mathrm{:}\\\text{n-step Sarsa}\longleftarrow&G_{t}^{(n)}=R_{t+1}+\gamma R_{t+2}+\cdots+\gamma^{n}q_{\pi}(S_{t+n},A_{t+n}),\\&\mathrm{:}\\\mathsf{MC}\longleftarrow&G_{t}^{(\infty)}=R_{t+1}+\gamma R_{t+2}+\gamma^{2}R_{t+3}+\ldots\end{aligned}
$$
Sarsa 的目标是解贝尔曼方程：$q_{\pi}(s,a)=\mathbb{E}[G_{t}^{(1)}|s,a]=\mathbb{E}[R_{t+1}+\gamma q_{\pi}(S_{t+1},A_{t+1})|s,a]$ 

MC learning 的目标是解贝尔曼方程：$q_\pi(s,a)=\mathbb{E}[G_t^{(\infty)}|s,a]=\mathbb{E}[R_{t+1}+\gamma R_{t+2}+\gamma^2R_{t+3}+\ldots|s,a]$ 

n-step Sarsa 的目标是解贝尔曼方程：
$$
q_\pi(s,a)=\mathbb{E}[G_t^{(n)}|s,a]=\mathbb{E}[R_{t+1}+\gamma R_{t+2}+\cdots+\gamma^nq_\pi(S_{t+n},A_{t+n})|s,a]
$$


所以 n-step Sarsa 算法的表达式为：
$$
\begin{aligned}q_{t+1}(s_{t},a_{t})&=q_{t}(s_{t},a_{t})-\alpha_{t}(s_{t},a_{t})\left[q_{t}(s_{t},a_{t})-\left(r_{t+1}+\gamma r_{t+2}+\cdots+\gamma^{n}q_{t}(s_{t+n},a_{t+n})\right)\right]\end{aligned}
$$
性质分析：

 1. ==**所有的随机近似算法都需要数据**==，n-step Sarsa 需要的数据是 
    $$
    (s_{t},a_{t},r_{t+1},s_{t+1},a_{t+1},\ldots,r_{t+n},s_{t+n},a_{t+n})
    $$

 2. 由于 $(r_{t+n},s_{t+n},a_{t+n})$ 在 $t$ 时刻还没有被收集到，无法在 $t$ 时刻立即使用 n-step Sarsa，而是==需要等到 $t+n$ 时刻才能更新 $(s_t,a_t)$ 的 action value 预测值==
    $$
    \begin{aligned}q_{t+n}(s_{t},a_{t})&=q_{t+n-1}(s_{t},a_{t})\\&-\alpha_{t+n-1}(s_{t},a_{t})\left[q_{t+n-1}(s_{t},a_{t})-\left(r_{t+1}+\gamma r_{t+2}+\cdots+\gamma^{n}q_{t+n-1}(s_{t+n},a_{t+n})\right)\right]\end{aligned}
    $$

 3. Sarsa 和 Monte-Carlo 是 n-step Sarsa 的两个极端，所以 n-step Sarsa 的性质自然混合了两者：

    当n比较大时，接近于 Monte-Carlo，方差大而误差小

    当n比较小时，接近于 Sarsa，误差相对较大（由初始值引起）而方差相对较小

 4. n-step 的本质还是在进行 Policy evaluation，要和 Policy improment 结合才能迭代出最优策略

### TD learning of optimal action values: Q-learning

==*直接估计最优 action value，不用在 policy evaluation 和 policy improvement 中交替运行*==

#### Algorithm

$$
\begin{aligned}q_{t+1}(s_t,a_t)&=q_t(s_t,a_t)-\alpha_t(s_t,a_t)\left[q_t(s_t,a_t)-[r_{t+1}+\gamma\max_{a\in\mathcal{A}}q_t(s_{t+1},a)]\right]\\q_{t+1}(s,a)&=q_t(s,a),\quad\forall(s,a)\neq(s_t,a_t)\end{aligned}
$$

与 Sarsa 及其相似，区别为：

1. Q-learning 的 TD target 是 $r_{t+1}+\gamma\max_{a\in\mathcal{A}}q_t(s_{t+1},a)$，Sarsa 的 TD target 是 $r_{t+1}+\gamma q_{t}(s_{t+1},a_{t+1})$ 

2. 在已知 $(s_t,a_t)$ 的条件下，Sarsa 在每次迭代中都需要计算出 $(r_{t+1},s_{t+1},a_{t+1})$，而Q-learning 只需要计算 $(r_{t+1}，s_{t+1})$

Q-learning 在数学上解决的问题是以下 ==**action value 形式的贝尔曼最优方程**==
$$
q(s,a)=\mathbb{E}\left[R_{t+1}+\gamma\max_{a}q(S_{t+1},a)|S_{t}=s,A_{t}=a\right]
$$
*为什么上式是一个贝尔曼**最优**方程，证明参见书P140*

#### Off-policy vs. On-policy

*这个问题不是仅仅针对于 Q-learning，而是对所有的强化学习算法都有*的一个分类标准

强化学习任务中存在两种 policy ：

​	Behavior policy - 按照此策略通过与环境交互不断生成 experience samples

​	Target policy - 不断被更新(evaluate+improvement)并最终收敛到最优策略

当一个算法的 Behavior policy 与 Target policy **相同**时被称作 **On-policy**，**不同**时被称作 **Off-policy** 

Off-policy 的优势：

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250515090558221.png" alt="image-20250515090558221" style="zoom:80%;" />

**如何判断一个强化学习算法是 Off-policy 还是 On-policy？** 

==首先看算法解决什么数学问题，然后看算法需要的 experience sample 的形式==

***Sarsa —— On-policy***

​	首先，Sarsa 的目标是解给定策略 $\pi$ 的贝尔曼方程，准确估计 $\pi$ 的 action value：
$$
q_\pi(s,a)=\mathbb{E}\left[R+\gamma q_\pi(S^{\prime},A^{\prime})|s,a\right]\quad\forall s,a.
$$
​	其中 $R\sim p(R|s,a),S^{\prime}\sim p(S^{\prime}|s,a),\color{red}A^{\prime}\sim\pi(A^{\prime}|S^{\prime})$；再与 policy improvement 结合得到 $\pi_t$，==**最终目的是将 $\pi_t$ 迭代为最优策略，所以 $\pi_t$ 是一个 Target policy**==

​	然后，具体算法形式为 $q_{t+1}(s_{t},a_{t})=q_{t}(s_{t},a_{t})-\alpha_{t}(s_{t},a_{t})\left[q_{t}(s_{t},a_{t})-(r_{t+1}+\gamma q_{t}(s_{t+1},a_{t+1}))\right]$  

​	需要的 sample 形式为 $(s_{t},a_{t},r_{t+1},s_{t+1},a_{t+1})$；在给定的 $(s_t,a_t)$ 下，**$r_{t+1},s_{t+1}$ 是通过采样给出的**因此与策略无关，而 ==**$a_{t+1}$ 是根据 $\pi_t(s_{t+1})$ 生成的，所以 $\pi_t$ 是一个 Behavior policy**== 

​	综上，$\pi_t$ 既是 Behavior policy，又是 Target policy，因此 Sarsa 是一个 On-policy 算法，流程图如下：
$$
\pi_t\to experience \to estimation\ of\ q_{\pi_t} \to \pi_{t+1}
$$
​	用 $\pi_t$ 生成数据，再用这些数据估计其 action value，再用得到的 action value 去改进 $\pi_t$ 得到 $\pi_{t+1}$ 

***Monte-carlo —— On-policy***

​	首先，MC方法的目标为估计给定策略 $\pi$ 的 action value
$$
q_{\pi}(s,a)=\mathbb{E}\left[R_{t+1}+\gamma R_{t+2}+\ldots|S_{t}=s,A_{t}=a\right]\quad\forall s,a.
$$
​	然后，具体运用中每计算完一个 episode 的 discounted return 之后就估计一次 action value：
$$
q(s,a)\approx r_{t+1}+\gamma r_{t+2}+\ldots\\
$$
​	其中需要的 episode 是依据 $\pi$ 生成的，用 episode 的信息来估计 action value，再用估计的 action value 来改进更新 $\pi$，所以显然 $\pi$ 既是 Behavior policy，又是 Target policy，因此 MC 是一个 On-policy 算法

 ***Q-learning —— Off-policy***

​	首先，Q-learning 的目标是解贝尔曼最优方程：
$$
q(s,a)=\mathbb{E}\left[R_{t+1}+\gamma\max_{a}q(S_{t+1},a)|S_{t}=s,A_{t}=a\right]\quad\forall s,a
$$
​	容易看出**贝尔曼最优方程没有显示地包含任何策略**

​	然后看具体算法形式：
$$
q_{t+1}(s_t,a_t)=q_t(s_t,a_t)-\alpha_t(s_t,a_t)\left[q_t(s_t,a_t)-[r_{t+1}+\gamma\max_{a\in\mathcal{A}}q_t(s_{t+1},a)]\right]
$$
​	需要的 sample 形式为 $(s_t,a_t,r_{t+1},s_{t+1})$ ，在给定的 $(a_t,s_t)$ 下得到 $r_{t+1},s_{t+1}$ 只依赖于环境而不依赖于任何策略！

​	因此==**由 $s_t$ 生成 $a_t$ 所依据的 Behavior policy 可以是任何策略**==，可以与 Target policy 相同也可以不同

#### Implementation

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250515093613557.png" alt="image-20250515093613557" style="zoom:80%;" />

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250515094037983.png" alt="image-20250515094037983" style="zoom:80%;" />

注意**两种实现方式目标的区别**：一个找从某状态出发到达目标状态的最优路径，一个找所有状态的最优策略

#### Examples

基于探索性很强的 Behavior policy，Target policy最终可以迭代到很接近最优策略

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250515094344002.png" alt="image-20250515094344002" style="zoom:80%;" />

而如果 Behavior policy 的探索性较弱，就会导致无法收敛到最优策略

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250515094406631.png" alt="image-20250515094406631" style="zoom:80%;" />

### Unified viewpoint and summary

所有的 TD 算法都可以统一为以下表达形式，只是不同的算法由不同的 TD target $\bar{q_t}$：
$$
q_{t+1}(s_t,a_t)=q_t(s_t,a_t)-\alpha_t(s_t,a_t)[q_t(s_t,a_t)-\color{red}\bar{q}_t\color{black}]
$$
<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250515092011991.png" alt="image-20250515092011991" style="zoom:80%;" />

同样，所有的算法都可以被视作解贝尔曼方程/贝尔曼最优方程的随机近似算法，仅 $R_{t+1}$ 的表达形式不同：

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250515092320560.png" alt="image-20250515092320560" style="zoom:80%;" />

## Chapter-8 Value Function Approximation

### Motivating-example：Curve Fitting

之前学习的都是 *tabular* ，即用表格记录 state/action values

![image-20250527095215427](F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250527095215427.png)

​	这虽然直观，但有两大问题：1. 受存储空间限制，无法解决 (s,a) pair 数量级很大的问题 2. 泛化能力弱，只有访问每一个 (s,a) pair 才能估计它们的值，但数量级很大时无法完全访问

​	**用一个曲线来拟合所有的点，纵轴为 $v_\pi(s)$，横轴为 $s$ , $\pi$ 是已知的**

​	优势在于==**需要存储的数据大大减少**==，比如使用最简单的线性拟合时，只需要存储 $w^T=[a,b]$ 两个参数
$$
\hat{v}(s,w)=as+b=\underbrace{[s,1]}_{\phi^T(s)}\underbrace{\begin{bmatrix}a\\b\end{bmatrix}}_{w}=\phi^T(s)w
$$
​	$w$ 称为**参数向量**，$\phi(s)$ 称为 $s$ 的**特征向量**；代价是对于值的估计(拟合精度)不够准确，这可以通过提高维数来改善,但相应地，要存储的数据也会随维数增加
$$
\hat{v}(s,w)=as^2+bs+c=\underbrace{[s^2,s,1]}_{\phi^T(s)}\underbrace{\begin{bmatrix}a\\b\\c\end{bmatrix}}_{w}=\phi^T(s)w.
$$
​	注意这里的估计函数 $\hat{v}(s,w)$ 仍是 $w$ 的线性函数	

​	==**泛化能力**==的直观解释：当我们使用拟合方法来估计各状态的值时，访问一个状态后更新的是权重 $w$ 而不是整个状态的估计值本身，所以其他**未被访问**状态的估计值**也会随着 $w$ 的更新而更新**

### Algorithm for value estimation

#### Objective Function

​	$v_\pi(s)$ 代表 $s$ 的 state value 的真实值，$\hat{v}(s,w)$ 代表其估计值，我们的目标就是**找到最优的 $w$ **让估计值尽可能接近真实值

​	这其实是一个 policy evaluation 问题，即给定策略 $\pi$，尽可能准确地估计其各状态 state value

​	找最优 $w$ 需要两步：1. 定义目标函数  2. 优化目标函数

​	目标函数定义为：
$$
J(w)=\mathbb{E}[(v_\pi(S)-\hat{v}(S,w))^2]
$$
​	我们的目标就是找到使得目标函数最小化的 $w$ 

​	目标函数中涉及到了随机变量 $S\in\mathcal{S}$，那么其概率分布 probability distribution 是什么样的呢？

1. 平均分布 uniform distribution

   **所有状态都被认为是平等重要**的，即把每一个状态的概率都设为 $1/|\mathcal{S}|$，在此条件下目标函数可化为：
   $$
   J(w)=\mathbb{E}[(v_\pi(S)-\hat{v}(S,w))^2]=\frac{1}{|\mathcal{S}|}\sum_{s\in\mathcal{S}}(v_\pi(s)-\hat{v}(s,w))^2
   $$
   但问题在于将所有状态视为平等重要显然是不符实际的，应该给那些靠近目标状态的**重要状态更高的权重**，这样子最终对他们 value 的估计误差就更小，而那些不重要状态的估计误差稍大也无所谓

2. 平稳分布 stationary distribution

   平稳分布描述了马尔可夫过程的 long-run behavior，即从一个状态出发，按照一个策略不断地采取 action 与环境交互，这一过程持续很久很久之后会达到一种**平稳状态**，此时可以获知 **agent 在每一个状态出现的概率**是多少

​	用 $\{d_\pi(s)\}_{s\in\mathcal{S}}$ 表示策略 $\pi$ 下的马尔可夫过程平稳分布，根据定义有 $d_\pi(s)\geq0$  和 $\sum{d_\pi(s)}=1,s\in \mathcal{S}$，此时目标函数可化为：
$$
J(w)=\mathbb{E}[(v_\pi(S)-\hat{v}(S,w))^2]=\sum_{s\in\mathcal{S}}d_\pi(s)(v_\pi(s)-\hat{v}(s,w))^2
$$
​	这是一个加权平方误差；由于访问越频繁的状态 $d_\pi(s)$ 值越大，它们在目标函数中的权重也就越大

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250527111353310.png" alt="image-20250527111353310" style="zoom:80%;" />

​	稳态分布定义为==稳定状态时==的概率分布，可以表示为**稳态分布向量与转移矩阵相乘的结果不变**：
$$
d_\pi^T=d_\pi^TP_\pi
$$
​	这代表稳态分布向量是转移矩阵**对应于特征值1的左特征向量**，所以已知转移矩阵就可以求出稳态分布

#### Optimization algorithm and function selection

​	使用**梯度下降**算法：$w_{k+1}=w_k-\alpha_k\nabla_wJ(w_k)$

​	代入我们上一节推出的平稳分布下的目标函数，可以得到 true gradient：
$$
\begin{aligned}\nabla_{w}J(w)&=\nabla_w\mathbb{E}[(v_\pi(S)-\hat{v}(S,w))^2]\\&=\mathbb{E}[\nabla_w(v_\pi(S)-\hat{v}(S,w))^2]\\&=2\mathbb{E}[(v_\pi(S)-\hat{v}(S,w))(-\nabla_w\hat{v}(S,w))]\\&=-2\mathbb{E}[(v_{\pi}(S)-\hat{v}(S,w))\nabla_{w}\hat{v}(S,w)]\end{aligned}
$$
​	式中涉及到了梯度的期望，这在不知道随机变量的概率分布时是很难算的，结合目标函数的形式——优化一个期望函数，容易想到前面学习的随机梯度下降算法(SGD)，用 stochastic gradient 替代 true gradient 得到：
$$
w_{t+1}=w_t+\alpha_t(v_\pi(s_t)-\hat{v}(s_t,w_t))\nabla_w\hat{v}(s_t,w_t)
$$
​	其中 $s_t$ 是随机变量 $S$ 的采样，$2\alpha_k$ 融合为 $\alpha_t$；但这个算法还无法实际使用，因为其中含有我们未知的 state value 真实值 $v_\pi(s_t)$，而我们前面学习了两种使用样本来估计 state value 的方法，蒙特卡洛和TD

1.  使用蒙特卡洛

   $g_t$ 表示从 $s_t$ 出发的一个 episode 的 discounted return，可以用于估计近似 $v_\pi(s_t)$，算法转化为：
   $$
   w_{t+1}=w_t+\alpha_t(g_t-\hat{v}(s_t,w_t))\nabla_w\hat{v}(s_t,w_t)
   $$

2. 使用 TD

   基于 TD Learning 的思想，$r_{t+1}+\gamma\hat{v}(s_{t+1},w_t)$ 作为 TD target 可以被视作对于 $v_\pi(s_t)$ 的估计，算法转化为：
   $$
   w_{t+1}=w_t+\alpha_t\left[r_{t+1}+\gamma\hat{v}(s_{t+1},w_t)-\hat{v}(s_t,w_t)\right]\nabla_w\hat{v}(s_t,w_t)
   $$
   <img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250527132015485.png" alt="image-20250527132015485" style="zoom:80%;" />

   linear case 指的是 $\hat{v}(s,w)$ 对于 $w$ 是线性的，可以表示为 $\hat{v}(s,w)=\phi^T(s) w$

#### Selection of function approximators

​	即选择如何选择 $\hat{v}(s,w)$ 的表达式

1. 使用线性函数
   $$
   \hat{v}(s,w)=\phi^T(s)w
   $$
   其中 $\phi(s)$ 是特征向量，可以选择为基于多项式、基于傅里叶级数等等

2. 使用神经网络

   使用神经网络拟合出来的是 nonlinear function approximator，是一个 $w$ 的**非线性函数**

   <img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250527133731440.png" alt="image-20250527133731440" style="zoom:80%;" />

#### Illustrative examples and analysis

​	下面这个例子是尝试使用 T-D Linear 方法估计一个给定策略的 state value

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250527135749363.png" alt="image-20250527135749363" style="zoom:80%;" />

​	上图展示的是 ground truth，三维图的x-y轴坐标代表每个 state 在方格世界中的位置，z轴代表其 value

![image-20250527135944435](F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250527135944435.png)

​	这是使用 tabular TD algorithm 方法的结果，和 ground truth 非常接近

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250527140055303.png" alt="image-20250527140055303" style="zoom:80%;" />

​	(a)图的特征向量为三维 $[1,x,y]^T$，对应的结果是平面，即
$$
\hat{v}(s,w)=\phi^T(s)w=[1,x,y]\begin{bmatrix}w_1\\w_2\\w_3\end{bmatrix}=w_1+w_2x+w_3y
$$
​	(b)图、(c)图的特征向量分别是六维 $[1,x,y,x^2,y^2,xy]^T$ 和十维 $[1,x,y,x^2,y^2,xy,x^3,y^3,x^2y,xy^2]^T$，可以发现随着特征向量维数增多，拟合效果是越来越好的 

​	linear的函数结构导致无法通过不断增加特征向量维度就让拟合误差减小到0，这也是为何现在都用神经网络

#### Summary of the story

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250527140958503.png" alt="image-20250527140958503" style="zoom:80%;" />

### Sarsa with function approximation

$$
w_{t+1}=w_{t}+\alpha_{t}\left[r_{t+1}+\gamma\hat{q}(s_{t+1},a_{t+1},w_{t})-\hat{q}(s_{t},a_{t},w_{t})\right]\nabla_{w}\hat{q}(s_{t},a_{t},w_{t})
$$

​	与使用 function approximation 的 TD learning 算法相比只是估计值从 state value 变为了 action value，即 $\hat{v}(s,w)$ 变为了 $\hat{q}(s,a,w)$

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250621003020692.png" alt="image-20250621003020692" style="zoom:80%;" />

### Q-Learning with function approximation

$$
w_{t+1}=w_{t}+\alpha_{t}\left[r_{t+1}+\gamma\color{red}\max_{a\in\mathcal{A}(s_{t+1})}\color{black}\hat{q}(s_{t+1},a,w_{t})-\hat{q}(s_{t},a_{t},w_{t})\right]\nabla_{w}\hat{q}(s_{t},a_{t},w_{t})
$$

<img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250621230451548.png" alt="image-20250621230451548" style="zoom:80%;" />

### Deep Q-learning (DQN)

将深度神经网络引入强化学习的最成功算法

Deep Q-learning 的目标是**最小化**下述目标函数（损失函数）：
$$
J(w)=\mathbb{E}\left[\left(R+\gamma\max_{a\in\mathcal{A}(S^{\prime})}\hat{q}(S^{\prime},a,w)-\hat{q}(S,A,w)\right)^2\right]
$$
​	其中 $(S,A,R,S')$ 是随机变量，如果使用梯度下降法来优化这个函数，计算$\max_{a\in\mathcal{A}(S^{\prime})}\hat{q}(S^{\prime},a,w)$ 的梯度需要一些技巧

​	我们要引入两个神经网络， 一个 **main network** 用来表示 $\hat{q}(s,a,w)$，即根据输入的 $s,a$ 和训练得到的网络参数 $w$ 对 action value 进行估计；一个 **target network** 用来表示 $\hat{q}(s,a,w_T)$，$w_T$ 不像 $w$ 一样是每输入一对 $(s,a)$ 就实时更新的，而是==**认为其在很短的时间内保持不变**==；然后损失函数就转化为：
$$
J(w)=\mathbb{E}\left[\left(R+\gamma\max_{a\in\mathcal{A}(S^{\prime})}\color{red}\hat{q}(S^{\prime},a,w_T)\color{black}-\color{blue}\hat{q}(S,A,w)\color{black}\right)^2\right]
$$
​	当 $w_T$ 固定不变时，$J$ 的梯度在舍去常系数之后就可以化为：
$$
\nabla_wJ=-\mathbb{E}\left[\left(R+\gamma\max_{a\in\mathcal{A}(S^{\prime})}\hat{q}(S^{\prime},a,w_T)-\hat{q}(S,A,w)\right)\nabla_w\hat{q}(S,A,w)\right]
$$
​	使用以上梯度表达式来最小化损失函数需要注意以下两个技巧：

1. 如前所述，要使用两个神经网络，它们的参数分别用 $w$和$w_T$ 表示，$w$和$w_T$ 一开始被设置为相同的初始值

   在每次迭代中，要从 *replay buffer* 中抽出一小批样本 $\{(s,a,r,s')\}$ 

   main network 的输入为 $(s,a)$，输出为 $y=\hat{q}(s,a,w)$

   而输出的目标值定义为 $y_{T}\doteq r+\gamma\max_{a\in\mathcal{A}(s^{\prime})}\hat{q}(s^{\prime},a,w_{T})$ 

   ==训练 main network 就是使用样本 $\{(s,a,y_T)\}$ 来最小化代价函数 $\sum(y-y_T)^2$，相当于把 $y_T$ 当作 label==

   在设定数量的迭代次数中 $w_T$ 保持不变，然后将迭代得到的 $w$ 赋值给 $w_T$，再重复以上过程

2. 经验回放 *experience replay*：我们收集到许多 experience sample，但并不需要按照收集的顺序使用它们

   因此将所有的样本存储在一个集合 $\mathcal{B}\doteq\{(s,a,r,s^{\prime})\}$ 中，称之为 *replay buffer*

   每次训练 main network 的时候就从 $\mathcal{B}$ 中**服从均匀分布**地抽出一小批样本，这个抽取过程就称为 *experience replay*

   为什么在DQN中要使用经验回放，回放过程又为什么一定要服从均匀分布呢？

   观察损失函数 $J=\mathbb{E}\left[\left(R+\gamma\max_{a\in\mathcal{A}(S^{\prime})}\hat{q}(S^{\prime},a,w)-\hat{q}(S,A,w)\right)^2\right]$ 中的随机变量：

   ​        $(S,A)\sim d{:}$ $(S,A)$ 视作一个索引，是一个单随机变量，服从某种分布 $d$

   ​        $R\sim p(R|S,A),S^{\prime}\sim p(S^{\prime}|S,A){:}$ $R$ 和 $S$ 由系统模型决定

   ​        在**没有先验知识**（比如知道哪些状态动作对更重要）的前提下，**要求**$(S,A)$ 必须一视同仁，概率全部相同，满足均匀分布

   ​        尽管在数学上要求 $(S,A)$ 均匀分布，但在采集数据时一定是按照其他的概率分布且有先后顺序的

   ​        因此要使用 *replay buffer* ==**打散所有样本然后从中均匀抽样**==，从而打破样本之间的相关性

   <img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250622090933738.png" alt="image-20250622090933738" style="zoom:80%;" />

   #### Illustrative examples

   详细的实验参数设置以及网络架构参见书P184-185

   <img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250622092628668.png" alt="image-20250622092628668" style="zoom:80%;" />

   <img src="F:\王梓恒\学习资料\Machine_Learning\Reinforcement_Learnig\Notes\images\image-20250622092707655.png" alt="image-20250622092707655" style="zoom:80%;" />

   ​        一个重要的误区：训练神经网络总是能保证 loss function 收敛，逼近你用来训练它的数据集，==**但收敛不代表最终得到的结果就是正确的**==，这说明再强大的算法也必须要有好的数据


## Chapter-9 Policy Gradient Methods

从 value-based 到 policy-based，用**函数**来表达策略，通过优化策略的目标函数直接得到最优策略

### Basic idea of policy gradient











