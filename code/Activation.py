from math import exp

def heaviside(x):
    if x > 0:
        return 1
    return 0

def relu(x):
    return max(0.0, x)

def sigmoid(x):
    return 1.0 / (1 + exp(-x))