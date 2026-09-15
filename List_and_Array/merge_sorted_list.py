def merge_sorted(a,b):
    result, i, j = [], 0, 0
    while i<len(a) and j <len(b):
        if a[i] <= b[j]:
            result.append(a[i]); i+=1
        else:
            result.append(b[j]); j+=1
    return result + a[i:] + b[j:]

print(merge_sorted([1,2,3,4,5],[2,3,4,5,6,7]))