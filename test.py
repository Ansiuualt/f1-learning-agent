import gymnasium as gym
from stable_baselines3 import PPO

# 1. Load the Environment
# render_mode="human" allows us to see the window popup
env = gym.make("CarRacing-v3", render_mode="human")

# 2. Load the Trained Model
model_path = "models/f1_driver_v1"
print(f"Loading model from {model_path}...")

try:
    model = PPO.load(model_path, env=env)
except FileNotFoundError:
    print("Error: Model not found! Did you run train.py first?")
    exit()

# 3. Run the Simulation
obs, _ = env.reset()
done = False

print("Press 'Ctrl+C' to stop the simulation.")
while True:
    # The model predicts the best action based on the current observation
    action, _states = model.predict(obs, deterministic=True)
    
    # Take the action in the environment
    obs, reward, terminated, truncated, info = env.step(action)
    
    # If the car crashes or finishes or time runs out, reset
    if terminated or truncated:
        obs, _ = env.reset()

env.close()