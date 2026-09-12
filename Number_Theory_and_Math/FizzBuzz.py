n = int(input("Enter the range: "))

# for i in range(1,n+1):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%5==0:
#         print("Buzz")
#     elif i%3==0:
#         print("Fizz")
#     else:
#         print(i)

for i in range(1,n+1):
    print("FizzBuzz" if i%15==0 else "Fizz" if i%3==0 else "Buzz" if i%5==0 else i, end = "-")
    
    