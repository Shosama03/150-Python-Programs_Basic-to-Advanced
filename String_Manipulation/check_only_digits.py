def is_all_digits(s):
    return all(c.isdigit() for c in s)

print(is_all_digits("12345"))
print(is_all_digits("123a45"))
