# gym_trading/trading_env.py
import gym
import numpy as np 
## 环境定义
class TradingEnvironment(gym.Env):
    def __init__(self, data):
        # 录入数据集
        self.df = data.set_index("Date") 
        # 收益统计参数
        self.profit_status = 0 
        self.total_profit = 0
        # 初始化状态
        self.state = self.df.iloc[0] 
    def step(self, action):
        # 执行买入/卖出/持有动作
        next_state = self.df.iloc[self.state.name + 1] 
        reward = 0
        done = False
        if action == 0: # 买入
            self.profit_status = 1   
            reward = (next_state["Close"] - self.state["Close"]) / self.state["Close"]    
        elif action == 1 and self.profit_status == 1: # 卖出
            reward = (next_state["Close"] - self.state["Close"]) / self.state["Close"] 
            self.profit_status = 0
            done = True # 回合结束
        self.total_profit += reward
        self.state = next_state # 状态转移
        if self.state.name == len(self.df) - 1: # 数据集到达末尾,游戏结束 
            done = True
        return self.state, reward, done, {}
    def reset(self):
        # 重置环境状态和参数
        self.total_profit = 0
        self.profit_status = 0
        self.state = self.df.iloc[0] 
        return self.state
    def render(self, mode='human'):
        # 打印收益情况
        print(f"回合收益: {self.total_profit}")