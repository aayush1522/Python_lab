# Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives
import numpy as np
result = np.empty(30)
result[:10] = 0   
result[10:20] = 1  
result[20:30] = 5  
print(result)


# Output: [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]
