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

# Add A and B element-wise
C = A + B

# Get the end time
toc = time.perf_counter()

# Subtract times to get total
np.set_printoptions(25)
print(np.array([toc - tic]))
