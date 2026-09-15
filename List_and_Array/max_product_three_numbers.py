# To find the maximum product of three numbers
def max_product(arr):
    arr.sort()
    return max(arr[-1]*arr[-2]*arr[-3], arr[0]*arr[1]*arr[-1])

print(max_product([-10,-10,5,2]))