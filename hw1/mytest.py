import numpy as np

# Create a Row Vector
a = np.matrix([1,2,3])

# Create a Column Vector
b = np.matrix([1,2,3]).transpose()

# Outer Product of Column Vector and Row Vector Creates Matrix
A = b*a

# Create a 3x3 Identity Matrix
I = np.identity(3)

# Add Two Matrices
B = I + A

# Solve for Bx = b
x = np.linalg.solve(B, b)

# Print the Solution
print(x)