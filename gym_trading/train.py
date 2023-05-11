# gym_trading/train.py
import os
import pandas as pd
import gym
import tensorflow as tf
from trading_env import TradingEnvironment 
from models import MyModel

def compute_loss(model, tape, obs, rewards, target_obs, q_next, dones, target_model, n_actions, gamma):  
    tape = tf.GradientTape()
    rewards = env.rewards  
    target_obs = env.target_obs
    q_next = model(target_obs, training=False) 
    dones = env.dones     
    target_model = model   
    n_actions = env.action_space.n 
    gamma = 0.99
    
    # 定义loss函数
    actions = model(obs, training=True)
    target_Q = target_model(target_obs, training=False)
    actions = tf.one_hot(actions, depth=n_actions)
    Q_values = tf.reduce_sum(target_Q * actions, axis=2)
    loss = tf.losses.MSE(Q_values, rewards + gamma * q_next * (1 - dones))

    loss_metrics(loss) # 统计loss指标,用于评估训练效果
    return loss

def train():
    # 获取项目根目录
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 加载数据并创建环境
    data_file = os.path.join(project_root, "gym_trading", "processed_data.csv")
    df = pd.read_csv(data_file)
    env = TradingEnvironment(df)
    # 创建模型
    obs_dim = env.observation_space.shape[0]
    model = MyModel(obs_dim, hidden_dim=512) 
    
    # 定义训练循环
    for epoch in range(100): # 训练100个epoch
        obs = env.reset() # 重置环境,获取初始观察值
        done = False
        total_reward = 0 # 统计 episode 总奖励
        while not done:
            # 计算行为并执行
            action = model(obs[tf.newaxis,:], training=True)
            obs, reward, done, info = env.step(action)
            # 增强学习
            with tf.GradientTape() as tape:
                total_reward += reward
                # 更新目标
                model_loss = compute_loss(model, tape, obs, rewards, target_obs, q_next, dones, 
                         target_model, n_actions, gamma)
            grads = tape.gradient(model_loss, model.trainable_weights)
            optimizer.apply_gradients(zip(grads, model.trainable_weights))
        # 训练结束,打印episode总奖励
        print(f"Epoch {epoch} total reward: {total_reward}")

if __name__ == "__main__":  
    train() 