import pandas as pd
import numpy as np

# Simulate user data
np.random.seed(42)

n_users = 1000

data = pd.DataFrame({
    "user_id": range(n_users),
    "group": np.random.choice(["A", "B"], n_users),
    "time_spent": np.random.normal(50, 10, n_users),
    "clicked": np.random.choice([0, 1], n_users, p=[0.7, 0.3])
})

# Simulate better performance for Group B
data.loc[data["group"] == "B", "time_spent"] += 5
data.loc[data["group"] == "B", "clicked"] = np.random.choice([0, 1], sum(data["group"] == "B"), p=[0.6, 0.4])

# Summary
print("Average Time Spent:")
print(data.groupby("group")["time_spent"].mean())

print("\nClick Rate:")
print(data.groupby("group")["clicked"].mean())

import matplotlib.pyplot as plt

# Visualization
data.groupby("group")["time_spent"].mean().plot(kind="bar")
plt.title("Average Time Spent by Group")
plt.ylabel("Time Spent")
plt.show()

data.groupby("group")["clicked"].mean().plot(kind="bar")
plt.title("Click Rate by Group")
plt.ylabel("Click Rate")
plt.show()
