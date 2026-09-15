def find_pairs(arr,target):
    seen, pairs = set(), []
    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.append((complement,num))
        seen.add(num)
    return pairs

print(find_pairs([1,5,7,-1,5],6))    