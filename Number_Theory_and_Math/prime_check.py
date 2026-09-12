def prime_check(n):
    if n<2:
        return False
    return all(n%i for i in range(2,int(n**0.5)+1))

n = int(input("Enter the range: "))
for i in range(2,n+1):
    print(f"{i} is Prime: ",prime_check(i))