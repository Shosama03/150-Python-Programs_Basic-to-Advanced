# To check if two strings are rotations of each other

def is_rotation(s1,s2):
    return len(s1) == len(s2) and s2 in (s1+s1)

print(is_rotation("waterbottle","erbottlewat"))
print(is_rotation("hello","lohel"))
print(is_rotation("hello","olelh"))