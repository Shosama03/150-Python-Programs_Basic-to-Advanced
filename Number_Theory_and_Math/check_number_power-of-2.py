def is_power_of_two(n):
    return n > 0 and (n & (n-1)) == 0

for num in [1,2,3,16,18,1024]:
    print(f"{num} is power of 2: {is_power_of_two(num)}")
    