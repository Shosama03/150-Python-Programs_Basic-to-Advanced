def count_vc(s):
    vowels = sum(1 for c in s.lower() if c in "aeiou")
    consonants = sum(1 for c in s.lower() if c.isalpha() and c not in "aeiou")
    
    return vowels,consonants

v,c = count_vc("Hello World")
print(f"Vowels: {v} || Consonants: {c}")
    