def to_camel_case(s):
    words = s.split()
    return words[0].lower() + "".join((w.capitalize()) for w in words[1:])

print(to_camel_case("convert this to camel case"))