def digit_sum(n):
    s = str(n)
    
    return sum(int(d) for d in str(abs(n)))


for num in [121,155,723,6134,532,123]:
    print(f"{num} sum = ",digit_sum(num))
    