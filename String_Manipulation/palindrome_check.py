def is_palindrome(s):
    s = s.lower().replace(" ","")
    return s == s[::-1]


print(is_palindrome("racecar"))
print(is_palindrome("nurses run"))
print(is_palindrome("hello"))