def arraycopy(arr):
    new = []
    for i in range(len(arr)):
        if isinstance(arr[i], list):
            new.append(arraycopy(arr[i]))
        else:
            new.append(arr[i])
    return new