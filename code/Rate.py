from math import exp

def decaying(x, n, decay_rate):
    return x / (1 + decay_rate * (n - 1))

def exponential(n, initial, decay_rate):
    return initial * exp(-decay_rate * n)