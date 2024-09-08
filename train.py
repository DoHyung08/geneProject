import gymnasium as gym

from stable_baselines3 import PPO
from stable_baselines3 import A2C
from stable_baselines3.common.env_util import make_atari_env
from stable_baselines3.common.vec_env import VecFrameStack
from geneEnv import geneEnv

env = geneEnv(1,20,100)
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10_000)