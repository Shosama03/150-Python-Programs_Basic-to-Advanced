def is_perfect(n):
    divisors = [i for i in range(1,n) if n%i == 0]
    return sum(divisors) == n

for num in [6,28,12,1245,123]:
    print(f"{num} is Perfect: {is_perfect(num)}")