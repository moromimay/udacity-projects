import numpy as np

def sigmoid(x):
    a = (1/(1 + np.exp(-x)))
    print a

sigmoid(0)
