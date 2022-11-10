import numpy as np
import scipy as sp


# matrix example
A = np.array([[2104, 3, 400],
              [1600, 3, 330],
              [2400, 3, 369],
              [1416, 2, 232],
              [3000, 4, 540],
              [1985, 4, 700],
              [1534, 3, 315],
              [1427, 3, 320],
              [1380, 3, 300],
              [1494, 3, 330],
              [1940, 4, 460],])

X = A[:, 0:2]
y = A[:, 2]

# print("A shape of a X: ", A.shape)


# norm of a vector
v = np.linalg.norm(X)
# print("magnitude of a matrix", v)

# initialuze theta
theta = np.zeros(2)

# Normal equation
theta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)

# print("Coefficients theta0 and theta1 :", theta)


# matrix with shape (3, 3)
A = np.array([[1, 0, 0],
            [-1, 1, 0],
            [0, -1, 1]]) 

x = np.array([1, 2, 3])

b = A.dot(x)
print(b)


inv_A = np.linalg.inv(A)
print(inv_A.dot(b))
