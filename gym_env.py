import gymnasium as gym
from gymnasium import spaces
import numpy as np
from traffic_env import TrafficEnv


class SumoGymEnv(gym.Env):
    metadata = {"render_modes": []}

    def __init__(self):
        super(SumoGymEnv, self).__init__()

        self.env = TrafficEnv()

        # Action space: 0 = NS green, 1 = EW green
        self.action_space = spaces.Discrete(2)

        # Observation space: queue length on 4 edges
        self.observation_space = spaces.Box(
            low=0,
            high=100,
            shape=(4,),
            dtype=np.float32
        )

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        state = self.env.reset()
        return state, {}

    def step(self, action):
        state, reward, terminated = self.env.step(action)
        truncated = False
        info = {}

        return state, reward, terminated, truncated, info

    def close(self):
        self.env.close()
