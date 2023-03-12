# Program to multiply two matrices using nested loops
import random
import numpy as np

N = 250

# NxN matrix
X = []
#for i in range(N):
#    X.append([random.randint(0,100) for r in range(N)])
X  = np.random.randint(100, size=(N,N))
# Nx(N+1) matrix
Y = []
#for i in range(N):
#    Y.append([random.randint(0,100) for r in range(N+1)])
Y = np.random.randint(100, size=(N,N+1))

# result is Nx(N+1)
result = []
result = np.dot(X,Y)

for r in result:
    #print(r)
    pass
