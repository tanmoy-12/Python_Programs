n=int(input("Enter the number of elements : "))
l1=[0 for _ in range(n)]
sum=0
for i in range(n):
    l1[i]=int(input("Enter the number : "))
for i in l1:
    if(i>=0):
        sum+=i
print("The sum of positive elements is ",sum)