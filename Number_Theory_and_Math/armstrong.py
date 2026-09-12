def armstrong(n):
    num_armstrong = str(n)
    
    return n == sum(int(d)**len(num_armstrong) for d in num_armstrong)


for num in [153,167,189,313,1779,9474]:
    print(f"{num} is Armstrong: ",armstrong(num))