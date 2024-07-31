import matplotlib.pyplot as plt

# Data
days = list(range(1, 32))
temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]

# Create the line chart
plt.figure(figsize=(12, 6))
plt.plot(days, temperature, marker='o', linestyle='-', color='b')
plt.xlabel('Days')
plt.ylabel('Temperature (°F)')
plt.title('Daily Temperature Changes Over Time')
plt.xticks(days, rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)

# Display the chart
plt.show()


#Conclusion
# This code uses the matplotlib library to create a line chart illustrating daily temperature variations over a month.
# It defines lists for the days and corresponding temperature values.
# The chart is configured with a 12x6 inch figure size, plotting the temperature data with blue lines and circle markers.
# Axis labels and a title are added to enhance clarity, with the x-axis labels rotated for better readability.
# A grid with dashed lines is included to improve visual separation.
# The resulting chart clearly depicts the temperature trends across the days, making it easy to interpret the data.
