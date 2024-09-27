# Optimized-tactile-sensor-model-for-shadow-hand-in-Gym-simulation
The project supply the XML file and a training policy for the Hand in OpenAI GYM. This sensor configuration reduce the sensor quantities from 92 to 21, but keep over 93% performance in block, egg and pen tasks.

Environment: Gym-0.2, Mujoco-150
Please put and replace "robot_touch_sensors_92" and "shared_touch_sensors_92" in this path: gym/envs/robotics/assests/hand
Then you can use command: test1.py to test if the new configuration takes effect.

A trained policy based on HER and DDPG is also offered. Before import the policy, you should install the HER By following link: https://github.com/TianhongDai/hindsight-experience-replay

After installing, put the "HandManipulateBlockTouchSensors-v0" floder in this path: hindsight-experience-replay/saved models

end.
