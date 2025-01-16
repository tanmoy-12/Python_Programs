def findMedian(l1,n):
    if(n%2==0):
        return (l1[n//2-1]+l1[n//2])/2
    else:
        return (l1[n//2])
n=int(input("Enter number of elements : "))
l1=[0 for _ in range(n)]
for i in range(n):
    l1[i]=int(input("Enter number : "))
print("The median of all the elements is : ",findMedian(l1,n))