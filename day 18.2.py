# 2. Suppose you have two sets of employee data—one containing information about full-time employees and another containing information about part-time employees. 
# You want to combine this data to create a comprehensive employee dataset for HR analysis.

import numpy as np

full_time_employees = np.array([
    [101, 'John Doe', 'Full-Time', 55000],
    [102, 'Jane Smith', 'Full-Time', 60000], 
    [103, 'Mike Johnson', 'Full-Time', 52000]
])

part_time_employees = np.array([
    [201, 'Alice Brown', 'Part-Time', 25000], 
    [202, 'Bob Wilson', 'Part-Time', 28000],
    [203, 'Emily Davis', 'Part-Time', 22000]
])

combined_employees = np.vstack((full_time_employees, part_time_employees))

print("Combined Employee Data:")
for employee in combined_employees:
    print(employee)

# Output:
# Combined Employee Data:
# ['101' 'John Doe' 'Full-Time' '55000']
# ['102' 'Jane Smith' 'Full-Time' '60000']
# ['103' 'Mike Johnson' 'Full-Time' '52000']
# ['201' 'Alice Brown' 'Part-Time' '25000']
# ['202' 'Bob Wilson' 'Part-Time' '28000']
# ['203' 'Emily Davis' 'Part-Time' '22000']
