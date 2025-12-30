import traci
import numpy as np


class TrafficEnv:
    def __init__(self):
        # Incoming edges to the intersection
        self.edges = [
            "north_center",
            "south_center",
            "east_center",
            "west_center"
        ]

        # Traffic light ID
        self.tls_id = "center"

        # Episode control
        self.max_steps = 1000
        self.current_step = 0

        # GUI flag (used by visual_test.py)
        self.use_gui = False

        self.sumo_running = False

    # ------------------------
    # SUMO control
    # ------------------------
    def start(self):
        """Start SUMO or SUMO-GUI safely"""

        if traci.isLoaded():
            traci.close()

        # Choose SUMO binary
        if self.use_gui:
            sumo_binary = r"C:\Program Files (x86)\Eclipse\Sumo\bin\sumo-gui.exe"
        else:
            sumo_binary = "sumo"

        traci.start([
            sumo_binary,
            "-c", "yournetwork.sumocfg",
            "--start",                # 🚨 REQUIRED so vehicles appear
            "--no-step-log", "true",
            "--no-warnings", "true"
        ])

        self.current_step = 0
        self.sumo_running = True

    def close(self):
        """Close SUMO safely"""
        if traci.isLoaded():
            traci.close()
        self.sumo_running = False

    # ------------------------
    # Environment API
    # ------------------------
    def reset(self):
        """Reset environment for a new episode"""
        self.start()
        return self.get_state()

    def step(self, action):
        """
        Action:
        0 -> North-South green
        1 -> East-West green
        """

        self.apply_action(action)

        # Advance simulation by one step
        traci.simulationStep()
        self.current_step += 1

        # Observe
        state = self.get_state()
        reward = self.compute_reward(state)

        done = self.current_step >= self.max_steps

        return state, reward, done

    # ------------------------
    # Helper functions
    # ------------------------
    def apply_action(self, action):
        """Apply traffic light phase"""
        if action == 0:
            traci.trafficlight.setPhase(self.tls_id, 0)  # NS green
        else:
            traci.trafficlight.setPhase(self.tls_id, 2)  # EW green

    def get_state(self):
        """State = queue length on each incoming edge"""
        state = [
            traci.edge.getLastStepHaltingNumber(edge)
            for edge in self.edges
        ]
        return np.array(state, dtype=np.float32)

    def compute_reward(self, state):
        """Reward = negative total queue length"""
        return -float(np.sum(state))
