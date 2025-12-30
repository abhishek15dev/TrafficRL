import time
import traci

MAX_STEPS = 1000
STEP_SLEEP = 0.1   # SAME as PPO

traci.start([
    r"C:\Program Files (x86)\Eclipse\Sumo\bin\sumo-gui.exe",
    "-c", "yournetwork.sumocfg"
])

tls = "center"
step = 0

while step < MAX_STEPS:
    traci.trafficlight.setPhase(tls, 0)  # NS green
    for _ in range(30):
        traci.simulationStep()
        time.sleep(STEP_SLEEP)
        step += 1
        if step >= MAX_STEPS:
            break

    traci.trafficlight.setPhase(tls, 2)  # EW green
    for _ in range(30):
        traci.simulationStep()
        time.sleep(STEP_SLEEP)
        step += 1
        if step >= MAX_STEPS:
            break

traci.close()
