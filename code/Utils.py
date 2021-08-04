def arraycopy(arr):
    new = []
    for i in range(len(arr)):
        if isinstance(arr[i], list):
            new.append(arraycopy(arr[i]))
        else:
            new.append(arr[i])
    return new

def rand_array(n, min=0.0, max=1.0):
    import random
    return [random.uniform(min, max) for _ in range(n)]

def flatten_2d(a):
    op = []
    for x in a:
        op += x
    return op

def deflatten_2d(a, width, height):
    if len(a) != width * height:
        raise ValueError("Length doesn't match give dimensions!")
    
    op = []
    for i in range(height):
        op.append(a[(i * width):(i * width + width)])
    return op

def default_vector(size, value):
    from Vector import Vector
    arr = [value] * size
    return Vector(arr)

def normalize(arr, min, max):
    op = []
    for x in arr:
        op.append((x - min) / (max - min))
    return op