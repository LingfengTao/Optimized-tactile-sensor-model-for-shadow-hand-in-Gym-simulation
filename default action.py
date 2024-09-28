import gym
import numpy as np

# Create the environment
env = gym.make('HandManipulateBlockTouchSensors-v0')

# Reset the environment to the initial state
obs = env.reset()

# Define a neutral action (e.g., all zeros for a stationary hand)
neutral_action = np.array([0.5,0,0,-1,-1,0,-1,-1,0,-1,-1,-1,0,-1,-1,0,0,0,0,0.5])

# Number of steps to render the stationary hand
num_steps = 10000

for step in range(num_steps):
    # Apply the neutral action to keep the hand stationary
    obs, reward, done, info = env.step(neutral_action)
    
    # Render the environment to visualize the hand
    env.render()

env.close()
