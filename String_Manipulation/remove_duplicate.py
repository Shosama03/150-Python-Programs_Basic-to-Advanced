def remove_dupe_chars(s):
    return "".join(dict.fromkeys(s))

print(remove_dupe_chars("Programming"))