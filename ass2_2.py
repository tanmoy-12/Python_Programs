def square_root(num):
    return int(num ** 0.5)
num = int(input("Enter the number : "))
root = square_root(num)
temp = root
count = 0
for i in range(1, temp+1):
    if(temp%i == 0):
        count+=1
if(count == 2):
    print("Square root of {num} is a prime")
else:
    print("Square root of {num} is not a prime")