import time
import numpy as np

num = 1000

# Make random matrices A and B
A = np.random.rand(num, 1)
B = np.random.rand(num, 1)

# Make empty array C of same dimensions
C = np.zeros((num, 1))

# Get the start time
tic = time.perf_counter()

# For all numbers from 0 to num
for i in range(num):
    # Set each index of C to be the value of that index at A plus B
    C.itemset((i), A.item(i) + B.item(i))

# Get the end time
toc = time.perf_counter()

# Subtract times to get total
print(toc - tic)