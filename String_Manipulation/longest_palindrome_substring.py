def longest_palindrome(s):
    best = ""
    for center in range(len(s)):
        for l,r in [(center, center), (center,center+1)]:
            while l>=0 and r < len(s) and s[l] == s[r]:
                l -=1
                r +=1
            if r - l - 1 > len(best):
                best = s[l+1:r]
    return best

print(longest_palindrome("babad"))