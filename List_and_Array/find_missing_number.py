def missing_number(arr):
    n = len(arr)
    expected = n * (n+1) // 2
    return expected - sum(arr)

print(missing_number([3,0,1]))