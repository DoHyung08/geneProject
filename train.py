import gymnasium as gym

from stable_baselines3 import PPO
#from stable_baselines3 import A2C
#from stable_baselines3.common.env_util import make_atari_env
from stable_baselines3.common.vec_env import VecFrameStack
from geneEnv import geneEnv



env = geneEnv(1,50,100)

# print(f"Observation space: {env.observation_space}")
# print(f"Action space: {env.action_space}")
# print(f"Sample observation: {env.reset()}")

model = PPO("MlpPolicy", env, verbose=1,device='cpu')
model.learn(total_timesteps=100_0000)
model.save("trained_model")