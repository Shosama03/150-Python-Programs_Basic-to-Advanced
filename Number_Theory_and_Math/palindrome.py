def palindrome(n):
    s = str(n)
    return s==s[::-1]


for num in [121,133,141,1661,787,1900]:
    print(f"{num} is Palindrome: ",palindrome(num))
    