from stable_baselines3 import PPO
from gym_env import SumoGymEnv

env = SumoGymEnv()

model = PPO(
    "MlpPolicy",
    env,
    verbose=1,
    tensorboard_log="./ppo_tensorboard/"
)

model.learn(total_timesteps=20000)

model.save("ppo_traffic")

env.close()
