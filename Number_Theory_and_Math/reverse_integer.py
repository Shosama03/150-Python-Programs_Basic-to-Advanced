def reverse_integer(n):
    sign = -1 if n< 0 else 1
    return sign * int(str(abs(n)))

print(reverse_integer(12345))
print(reverse_integer(-9876))