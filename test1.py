import gym

# Create the environment
env = gym.make('HandManipulateBlockTouchSensors-v0')

# Reset the environment to get the initial observation
obs = env.reset()

# Number of steps to run
num_steps = 10000

# Run the environment for a number of steps
for step in range(num_steps):
    # Sample a random action from the action space
    action = env.action_space.sample()
    
    # Take the action in the environment
    obs, reward, done, info = env.step(action)
    
    # Render the environment
    env.render()
    
    # Check if the episode is done
    if done:
        # Reset the environment if done
        obs = env.reset()

# Close the environment when done
env.close()

