
def quadratic(target, output):
    if len(target) != len(output):
        raise ValueError("Unequal lengths!")

    loss = 0.0
    for (t, o) in zip(target, output):
        loss += (t - o) ** 2
    return loss

def quadratic_d(t, o):
    return 2 * o - 2 * t

def mean_quadratic(x, y):
    return (1 / len(x)) * quadratic(x, y)

def mean_quadratic_d(t, o):
    return o - t