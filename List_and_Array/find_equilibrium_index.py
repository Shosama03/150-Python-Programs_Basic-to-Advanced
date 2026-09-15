def equilibrium_index(arr):
    total = sum(arr)
    left_sum = 0
    for i, num in enumerate(arr):
        total -= num
        if left_sum == total:
            return i
        left_sum += num
    return -1

print(equilibrium_index([-7,1,5,2,-4,3,0]))