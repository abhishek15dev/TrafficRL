import time
from gym_env import SumoGymEnv

env = SumoGymEnv()

# 🔴 Enable GUI
env.env.use_gui = True

obs, _ = env.reset()

MAX_STEPS = 1000   # match baseline
SLEEP_TIME = 0.1   # slow for recording

for step in range(MAX_STEPS):
    action = step % 2  # simple alternating policy (replace later with PPO)

    obs, reward, terminated, truncated, info = env.step(action)

    time.sleep(SLEEP_TIME)

    if terminated or truncated:
        break

env.close()
