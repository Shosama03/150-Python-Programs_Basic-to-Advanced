# Title-casing a sentence without using .title()
def my_title(s):
    return " ".join(word[0].upper() + word[1:].lower() for word in s.split())

print(my_title("the quick brown FOX"))