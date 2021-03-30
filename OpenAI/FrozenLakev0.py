import gym
env=gym.make('FrozenLake-v0')

num_episodes = 10
num_timesteps = 20
for i in range(num_episodes):
    state = env.reset()
    print('Time Step 0 :')
    env.render()
    for t in range(num_timesteps):
        random_action = env.action_space.sample()
        new_state, reward, done, info = env.step(random_action)
        print ('Time Step {} :'.format(t+1))
        env.render()
        if done:
            break