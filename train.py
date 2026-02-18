import gymnasium as gym
from stable_baselines3 import PPO
import os

# 1. Create the Environment
# "CarRacing-v3" is a top-down racing environment. 
# render_mode=None makes training faster (we don't need to see it while it learns)
env = gym.make("CarRacing-v3", render_mode=None)

# 2. Define Paths
model_dir = "models"
log_dir = "logs"

if not os.path.exists(model_dir):
    os.makedirs(model_dir)

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# 3. Initialize the Agent (The Model)
# We use PPO (Proximal Policy Optimization), a standard efficient RL algorithm.
# MlpPolicy uses standard dense neural networks. 
# CnnPolicy would be used if we were feeding raw pixels (images) instead of state data.
model = PPO("CnnPolicy", env, verbose=1, tensorboard_log=log_dir)

# 4. Train the Agent
TIMESTEPS = 100000  # Number of steps to learn. Higher = better driving, longer wait.
print(f"Training for {TIMESTEPS} timesteps...")

model.learn(total_timesteps=TIMESTEPS, progress_bar=True)

# 5. Save the Model
model_path = f"{model_dir}/f1_driver_v1"
model.save(model_path)
print(f"Model saved to {model_path}.zip")

env.close()