def second_largest(arr):
    return sorted(set(arr))[-2]

arr = [3,4,6,2,23,5,7,23,4,1,89,7,8,]
print(second_largest(arr))