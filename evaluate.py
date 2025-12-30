import time
from stable_baselines3 import PPO
from gym_env import SumoGymEnv

env = SumoGymEnv()
env.env.use_gui = True  # enable SUMO-GUI

model = PPO.load("ppo_traffic")

obs, _ = env.reset()

for step in range(500):
    action, _ = model.predict(obs, deterministic=True)
    obs, reward, terminated, truncated, info = env.step(action)

    time.sleep(0.1)  # slow for visualization

    if terminated or truncated:
        break

env.close()
