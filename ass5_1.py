n=int(input("Enter the number of items in the list : "))
l1=[0 for _ in range(n)]
for i in range(n):
    l1[i] = int(input("Enter number : "))
l2=[]
k=0
for i in range(0, n):
    flag=0
    for j in range(0, k):
        if l1[i] == l2[j]:
            flag=1
            break
    if(flag==0):
        k+=1
        l2.append(l1[i])
print("The list with unique elemenets is \n", l2)    