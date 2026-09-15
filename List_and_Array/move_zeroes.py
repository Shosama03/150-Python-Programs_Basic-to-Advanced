def move_zeros(arr):
    non_zeros = [x for x in arr if x!=0]
    return non_zeros + [0] * (len(arr) - len(non_zeros))

print(move_zeros([0,1,0,3,4,0,9]))