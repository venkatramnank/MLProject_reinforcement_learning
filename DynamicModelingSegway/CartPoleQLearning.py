import gym
import numpy as np 
import time
import matplotlib.pyplot as plt

env=gym.make('CartPole-v0')

# Contains the maximum reward obtained up to the current episode
HighReward=0

# BestWeights variable will contain sequence of weights that will have the maximum reward
BestWeights = None

scores=[]
for i in range(200):
    observation=env.reset()
    # sequence of weights equal in number to the observations of the environment, 
    # which is four (cart position, cart velocity, pole angle, and pole velocity at tip)
    Weights=np.random.uniform(-1,1,4)
    SumReward = 0
    for j in range(1000):
        env.render()
        #time.sleep(0.05)
        # if product is <0, the action is 0 (move left); otherwise, the action is 1 (move right)
        action = 0 if np.matmul(Weights,observation) < 0 else 1
        observation,reward,done,info = env.step(action)
        SumReward+= reward
        print(i,j,Weights,observation,action,SumReward,BestWeights)
    if SumReward > HighReward:
        HighReward = SumReward
        BestWeights = Weights
    scores.append(SumReward)
print(scores)

x=[i for i in range(200)]
plt.plot(x,scores)
plt.show()