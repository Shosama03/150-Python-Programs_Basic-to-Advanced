from collections import Counter

text = "the quick brown fox jumps over the lazy dog the fox runs"
count = Counter(text.split())
print(count.most_common(3))
