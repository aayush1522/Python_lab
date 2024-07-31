# 2. Calculate the profit made by a company

import numpy as np

# Revenue and expenses data
revenue = np.array([10000, 12000, 11000, 10500])
expenses = np.array([4000, 5000, 4500, 4800])

# Calculate the profit by subtracting expenses from revenue
profit = revenue - expenses

# Print the profit
print("Profit:", profit)

# Output:
# Profit: [6000 7000 6500 5700]
