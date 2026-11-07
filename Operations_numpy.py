import numpy as np
# 1. Creating an Array of linearly spaced elements from 0 to 9
record = np.linspace(0,9, 10)
print(record)

# 2. Replacing all odd numbers with -1
print(np.where(record % 2 != 0, -1, record))

# 3. Creating a new array that consists of 1-dimensional array converted into a 2-dimensional array, with 2 rows
arr = np.array([1,2,3,4,5,6,7,8])
print(arr.reshape(2,4))

# 4. Iterating through the original array and finding the sum of even numbers
sum_even_number = 0
for even_number in record:
    if even_number % 2 == 0:
        sum_even_number+=even_number
    else:
        continue
print(sum_even_number)
