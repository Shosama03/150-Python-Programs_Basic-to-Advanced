# to compress strings (aaabbb -> a3b3)

def compress(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i+1 < len(s) and s[i] == s[i+1]:
            i+=1
            count+=1
        result.append(s[i] + str(count) if count > 1 else "")
        i+=1
        
    return "".join(result)

print(compress("aaaaaabbbbbcccccddddddeeeeee"))