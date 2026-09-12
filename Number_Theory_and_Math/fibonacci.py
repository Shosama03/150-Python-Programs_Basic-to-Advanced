# 3 ways to find Fibonacci numbers
#input
n = int(input("Enter the number: "))


# First Method
def fib_loop(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b,a+b
    return a


# Second Method
def fib_recur(n):
    if n<=1:
        return n
    return fib_recur(n-1) + fib_recur(n-2)


# Third Method
def fib_memo(n,memo={}):
    if n in memo:
        return memo[n]
    if n<=1:
        return n
    memo[n] = fib_memo(n-1,memo) + fib_memo(n-2,memo)
    print(memo)
    return memo[n]


# Printing all three functions (Prints only One Number)
# print("Loop: ",fib_loop(n))
# print("Recursive: ",fib_recur(n))
# print("Memoized: ",fib_memo(n))

# print("---------------------------------------------------------------------------")
# # Printing all three functions (Prints Entire Range)
# print("Loop: ",[fib_loop(i) for i in range(n)])
# print("Recursive: ",[fib_recur(i) for i in range(n)])
print("Memoized: ",[fib_memo(i) for i in range(n+1)])
