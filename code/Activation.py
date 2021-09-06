from math import exp

def heaviside(x):
    if x > 0:
        return 1
    return 0

def relu(x):
    return max(0.0, x)

def relu_d(x):
    return heaviside(x)

def sigmoid(x):
    if x < 0:
        return 1 - 1 / (1 + exp(x))
    return 1 / (1 + exp(-x))

def sigmoid_d(x):
    return x * (1 - x)