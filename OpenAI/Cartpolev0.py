import gym
import time
env = gym.make('CartPole-v0')
env.mode='human'
num_episodes = 100
num_timesteps = 50

for i in range(num_episodes):
    Return=0
    state=env.reset()
    for t in range(num_timesteps):
        env.render()
        time.sleep(0.025)
        random_action = env.action_space.sample()
        next_state, reward, done, info = env.step(random_action)
        Return = Return + reward
        if done:
            break
        if i%10==0:
            print('Episode: {}, Return: {}'.format(i, Return))
