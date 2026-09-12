n = int(input("Enter the Number: "))

def fact_rec(n):
    return 1 if n<=1 else n*fact_rec(n-1)

def fact_iter(n):
    result = 1
    for i in range(2,n+1):
        result *=i
    return result

print(f"Recursive Factorial of {n}! ->",fact_rec(n))
print(f"Iterative Factorial of {n}! ->",fact_iter(n))