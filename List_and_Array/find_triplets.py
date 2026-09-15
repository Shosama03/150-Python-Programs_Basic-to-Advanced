# To find triplets that sum to zero

def three_sum(arr):
    arr.sort()
    result = []
    for i in range(len(arr)-2):
        if i > 0 and arr[i]==arr[i-1]:
            continue
        l,r = i+1, len(arr)-1
        while l<r:
            total = arr[i] + arr[l] + arr[r]
            if total == 0:
                result.append([arr[i],arr[l],arr[r]])
                l+=1; r-=1
            elif total<0:
                l += 1
            else:
                r -= 1
    return result

print(three_sum([-1,0,1,2,-1,-4]))