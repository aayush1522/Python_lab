import numpy as np

my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)

print("Original Array:")
print(my_array)

print("\nFirst Index:", my_array[0])
print("Last Index:", my_array[-1])

my_array *= 2

print("\nArray after multiplying each element by 2:")
print(my_array)

#output
Original Array:
[1 2 3 4 5]

First Index: 1
Last Index: 5

Array after multiplying each element by 2:
[ 2  4  6  8 10]
