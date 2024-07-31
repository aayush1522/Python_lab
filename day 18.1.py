# Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions.
# Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day).

import numpy as np
temperatures = np.array([12, 36.8, 7, 28, 4, 30, 40, 3, 20, 37.2, 15, -12, 25, -4])

hot_days = temperatures > 35
cold_days = temperatures < 5

hot_day_indices = np.where(hot_days)[0]
cold_day_indices = np.where(cold_days)[0]

print("Hot Days:")
print("Day\tTemperature (°C)")
for index in hot_day_indices:
    print(f"{index+1}\t{temperatures[index]}")

print("\nCold Days:")
print("Day\tTemperature (°C)")
for index in cold_day_indices:
    print(f"{index+1}\t{temperatures[index]}")

# Output:
# Hot Days:
# Day    Temperature (°C)
# 2      36.8
# 7      40.0
# 10     37.2
#
# Cold Days:
# Day    Temperature (°C)
# 5      4.0
# 8      3.0
# 12     -12.0
# 14     -4.0
