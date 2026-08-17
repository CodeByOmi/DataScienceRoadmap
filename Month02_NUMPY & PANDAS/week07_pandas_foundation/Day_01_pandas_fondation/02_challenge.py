import pandas as pd

gym_members = pd.DataFrame({
    "Name": [
        "Omkar", "Rahul", "Priya", "Amit", "Sneha",
        "Rohan", "Neha", "Vishal", "Pooja", "Karan"
    ],
    "Age": [
        21, 24, 22, 28, 20,
        26, 23, 30, 25, 27
    ],
    "Gender": [
        "Male", "Male", "Female", "Male", "Female",
        "Male", "Female", "Male", "Female", "Male"
    ],
    "Weight": [
        74.5, 82.0, 58.5, 90.0, 55.0,
        76.5, 62.0, 85.0, 60.5, 79.0
    ],
    "Height": [
        180, 175, 165, 182, 160,
        178, 168, 180, 163, 176
    ],
    "Membership": [
        "Premium", "Basic", "Premium", "Basic", "Premium",
        "Basic", "Premium", "Premium", "Basic", "Premium"
    ]
})

print(gym_members)
print(gym_members.head())
print(gym_members.head(3))
print(gym_members.tail())
print(gym_members.tail(2))
print(gym_members.shape)
print(gym_members.index)