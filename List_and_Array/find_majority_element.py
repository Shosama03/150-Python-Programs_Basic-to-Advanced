# This is also known as Boyer-Moore Voting

def majority_element(arr):
    count, candidate = 0, None
    for num in arr:
        if count == 0:
            candidate = num
        count +=1 if num == candidate else -1
    return candidate

print(majority_element([2,2,1,1,1,2,2,2,1,5,6,6]))