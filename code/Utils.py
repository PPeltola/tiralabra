def arraycopy(arr):
    return list(arr)

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
        raise ValueError("Length doesn't match given dimensions!")
    
    op = []
    for i in range(height):
        op.append(a[(i * width):(i * width + width)])
    return op

def default_vector(size, value):
    from Vector import Vector
    arr = [value] * size
    return Vector(arr)

def normalize(arr, minimum, maximum):
    op = []
    for x in arr:
        op.append((x - minimum) / (maximum - minimum))
    return op

def fit_arr(arr, minimum, maximum, mode='int'):
    narr = normalize(arr, min(arr), max(arr))
    op = []
    for x in narr:
        if mode == 'float':
            op.append(minimum + x * maximum)
        else:
            op.append(int(round(minimum + x * maximum)))
    return op

def onehot_label_arr(num):
    if num > 9:
        raise ValueError("Not a digit!")
    
    arr = [0] * 10
    arr[num] = 1
    return arr

def make_prediction(arr):
    largest = 0
    largest_i = 0
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            largest_i = i
    return largest_i