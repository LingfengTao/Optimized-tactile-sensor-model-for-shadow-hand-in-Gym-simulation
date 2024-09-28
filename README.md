# Optimized-tactile-sensor-model-for-shadow-hand-in-Gym-simulation
This project optimized the gym-0.20.0 default tactile sensor configuration for hand tasks.

**The project also supply an adding install version in another branch, if you already install the gym, you could directly use that branch.*

# Requirement
python = 3.6  
Mujoco = 150  
mujoco-py = 1.50.1.0  
gcc&g++ = 4.8  
Cython = 0.29.21  
opencv-python = 4.3.0.38  
HER (need for running demo)

# Installation
1. To install this optimized gym version, use  
`git clone https://github.com/WilliamAlexanda/Optimized-tactile-sensor-model-for-shadow-hand-in-Gym-simulation.git`

2. To install mjpro150, use this link: https://roboti.us/download.html  

3. To install mojoco-py, use  
`pip install mujoco-py==1.50.1.0`  
*Please follow this link to install the license: https://roboti.us/license.html*

4. (Optional) To install HER, please refer to this link: https://github.com/TianhongDai/hindsight-experience-replay  

# Test
1. After complete step 1~3, you could use `python test1.py` to see if the environment is correctly installed. If correct, the new window will show the dexterous hand with new tactile configuration.
2. After complete the step 4, you could put the "HandManipulateBlockTouchSensors-v0" into the saved_model floder of HER and use `python demo.py --env-name=HandManipulateBlockTouchSensors` to run the demo.

# Reference
https://github.com/openai/gym/tree/v0.20.0
