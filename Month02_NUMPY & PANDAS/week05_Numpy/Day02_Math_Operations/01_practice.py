import numpy as np

# 1.Arithmetic Operations
steps = np.array([8000, 9000, 10000, 11000, 9500])

print("Original:", steps)

print("Add 1000:", steps + 1000)

print("Subtract 500:", steps - 500)

print("Multiply by 2:", steps * 2)

print("Divide by 1000:", steps / 1000)


# 2.Statistical Operations
study_hours = np.array([4, 5, 6, 4, 5])

revision_hours = np.array([1, 1, 2, 1, 2])

total_hours = study_hours + revision_hours

print("Total Hours:", total_hours)



# 3.aggregate functions
water = np.array([4.5, 5, 4.8, 5.2, 4.7])

print("Total:", np.sum(water))

print("Average:", np.mean(water))

print("Maximum:", np.max(water))

print("Minimum:", np.min(water))


# 4.standard deviation
marks = np.array([78, 85, 90, 88, 82])

print("Standard Deviation:", np.std(marks))
