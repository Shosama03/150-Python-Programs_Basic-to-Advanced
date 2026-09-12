def power(base,exp):
    result = 1
    for _ in range(exp):
        result*=base
    return result

print(power(2,10))
print(power(3,16))