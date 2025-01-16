import numpy as np

x = [1, 2, 3]
M1 = np.array([x,x,x])
M2 = np.array([x,x,x])
print(M1.dot(M2))  # Output: [1 2 3 4 5]