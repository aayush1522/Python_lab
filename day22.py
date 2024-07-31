import matplotlib.pyplot as plt

# Data for the line plot
x = [0, 5, 9, 10, 15, 20, 25]
y = [0, 1, 2, 3, 4, 5, 6]

# Create a line plot
plt.figure(figsize=(10, 5))
plt.plot(x, y, marker='o')
plt.title("Line Plot of Given Data")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
