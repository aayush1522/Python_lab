import numpy as np
import matplotlib.pyplot as plt

# Data input
months = np.arange(1, 13)
electronics_sales = np.array([25000, 28000, 31000, 27000, 30000, 32000, 35000, 36000, 38000, 39000, 41000, 42000])
clothing_sales = np.array([15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000])
home_garden_sales = np.array([18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000])
sports_outdoors_sales = np.array([12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000])

# Plotting the sales performance
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Electronics
axs[0, 0].plot(months, electronics_sales, marker='o', color='blue')
axs[0, 0].set_title('Electronics Sales')
axs[0, 0].set_xlabel('Month')
axs[0, 0].set_ylabel('Sales ($)')
axs[0, 0].grid(True)

# Clothing
axs[0, 1].plot(months, clothing_sales, marker='o', color='green')
axs[0, 1].set_title('Clothing Sales')
axs[0, 1].set_xlabel('Month')
axs[0, 1].set_ylabel('Sales ($)')
axs[0, 1].grid(True)

# Home & Garden
axs[1, 0].plot(months, home_garden_sales, marker='o', color='red')
axs[1, 0].set_title('Home & Garden Sales')
axs[1, 0].set_xlabel('Month')
axs[1, 0].set_ylabel('Sales ($)')
axs[1, 0].grid(True)

# Sports & Outdoors
axs[1, 1].plot(months, sports_outdoors_sales, marker='o', color='orange')
axs[1, 1].set_title('Sports & Outdoors Sales')
axs[1, 1].set_xlabel('Month')
axs[1, 1].set_ylabel('Sales ($)')
axs[1, 1].grid(True)

# Adjust layout
plt.tight_layout()
plt.show()


#Conclusion
#Electronics: The sales show a steady increase over the months, peaking at $42,000 in December.
#This category has the highest sales overall, indicating strong and growing demand.
#Clothing: Sales steadily increase from $15,000 in January to $26,000 in December.
#This category shows consistent growth but at a slower pace compared to electronics.
#Home & Garden: Sales also show a steady rise, from $18,000 in January to $29,000 in December.
#The growth pattern is similar to clothing but at a slightly higher sales volume.
#Sports & Outdoors: Starting from $12,000 in January and reaching $23,000 in December,
#this category has the lowest sales but shows a consistent upward trend.
