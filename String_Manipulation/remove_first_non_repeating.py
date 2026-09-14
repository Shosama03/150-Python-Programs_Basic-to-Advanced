from collections import Counter

def first_unique(s):
    counts = Counter(s)
    for c in s:
        if counts[c] == 1:
            return c
    return None

print(first_unique("swiss"))
print(first_unique("aabbcc"))