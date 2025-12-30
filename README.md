# Traffic Signal Control using Reinforcement Learning (PPO)

This project demonstrates **traffic signal control at an intersection using Reinforcement Learning (PPO)** and compares it with a **fixed-time baseline controller** using the **SUMO traffic simulator**.

The goal is to reduce traffic congestion by dynamically controlling traffic lights based on queue lengths.

---

## Project Overview

- **Simulator**: SUMO (Simulation of Urban Mobility)
- **RL Algorithm**: Proximal Policy Optimization (PPO)
- **Framework**: Stable-Baselines3
- **Environment Interface**: Gymnasium + TraCI
- **Comparison**: PPO vs Fixed-Time Baseline

---

## Approach

### Baseline Controller
- Uses a **fixed-time traffic light cycle**
- Alternates between North-South and East-West green phases
- Does not adapt to traffic conditions

### PPO Controller
- Observes **queue lengths** on incoming roads
- Learns an **adaptive traffic signal policy**
- Objective: minimize total queue length

---

##  Project Structure

TrafficRL/
│
├── traffic_env.py # SUMO + TraCI traffic environment
├── gym_env.py # Gymnasium wrapper
├── train_ppo.py # PPO training script
├── evaluate.py # PPO evaluation script
├── visual_test.py # Visual PPO simulation
├── baseline_fixed.py # Fixed-time baseline controller
├── yournetwork.sumocfg # SUMO configuration file
├── yournetwork.net.xml # Network file
├── yournetwork.rou.xml # Route file
└── README.md



---

##  How to Run

### 1. Baseline Simulation
python baseline_fixed.py

 **2. PPO Visual Simulation**
python visual_test.py

**3. PPO Training (Optional)**
python train_ppo.py

**Results**
PPO adapts signal timing based on traffic conditions

Baseline follows a rigid schedule

PPO achieves lower average queue lengths over time

Demonstrated via side-by-side visual comparison

Demo Video
A demo video comparing:

Fixed-time baseline

PPO-controlled traffic lights
has been recorded and submitted as part of the evaluation.

**Author**
Abhishek
1st year Undergraduate Student at IIT Roorkee
Traffic Signal Optimization using Reinforcement Learning

**Notes**
SUMO must be installed and added to PATH

Python 3.9+ recommended

Project developed for academic evaluation


