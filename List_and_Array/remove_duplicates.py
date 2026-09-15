def remove_duplicate(arr):
    return list(dict.fromkeys(arr))

print(remove_duplicate([1,2,3,4,4,4,5,6,76,7,8,8,1,2,2,4]))