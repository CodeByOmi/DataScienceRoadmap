# personal health and productive analyzer

import numpy as np

steps = np.array([8500, 9200, 11000, 7600, 9800, 10500, 9000])

study = np.array([4, 5, 6, 4, 5, 4, 5])

water = np.array([4.5, 5.0, 4.8, 5.2, 4.7, 5.0, 4.9])

print("===== STEP ANALYSIS =====")
print("Average Steps:", np.mean(steps))
print("Highest Steps:", np.max(steps))
print("Days above 9000:", steps[steps > 9000])

print()

print("===== STUDY ANALYSIS =====")
print("Average Study Hours:", np.mean(study))
print("Days with 5+ Hours:", np.sum(study >= 5))

print()

print("===== WATER ANALYSIS =====")
print("Average Water Intake:", np.mean(water))
print("Median Water Intake:", np.median(water))