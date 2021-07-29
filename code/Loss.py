
def quadratic(x, y):
    if len(x) != len(y):
        raise ValueError("Unequal lengths!")

    loss = 0.0
    for (xi, yi) in zip(x, y):
        loss += (xi - yi) ** 2
    return loss