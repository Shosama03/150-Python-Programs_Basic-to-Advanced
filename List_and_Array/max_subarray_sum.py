# This is also known as Kadane's Algorithm

def max_subarray(arr):
    current = best = arr[0]
    for num in arr[1:]:
        current = max(num,current+num)
        best = max(best, current)
        
    return best

print(max_subarray([1,2,3,4,5,6,7,8]))