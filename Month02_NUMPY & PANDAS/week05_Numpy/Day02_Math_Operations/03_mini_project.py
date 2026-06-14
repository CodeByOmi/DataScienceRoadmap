# Weekly Productivity Analyzer

import numpy as np

study = np.array([4,4,5,3,6,5,4])

gym = np.array([1.5,2,1.5,2,1.5,2,1.5])

gaming = np.array([2,3,2,4,3,2,4])

steps = np.array([8500,1000,9000,8000,8100,9300,8200])

water_intake = np.array([5,5,6,6,5,7,5])

print("gaming hours:", gaming)

print("highest steps:", np.max(steps))

print("lowest study:", np.min(study))

print("avrage study:", np.mean(study))

print("lowest water intake:", np.min(water_intake))

print("lowest gaming:", np.min(gaming))

print(study + gym)

print("total steps:", np.sum(steps))
