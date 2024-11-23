def move_zeros(arr):

    if arr.count(0) == 0:
        return arr
    
    for _ in arr:
        arr.pop(arr.index(0))
        arr.append(0)
        
    return arr