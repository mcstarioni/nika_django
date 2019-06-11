import numpy as np

probability_A = 0.6


b = np.array([0.6, 0.4, 0], float)
d = np.array([[0.6, 0.3, 0.1],[0.4, 0.4, 0.2], [0.2, 0.3, 0.5]], float)
c=b*d
Z = np.dot(b,d)
print(Z)
