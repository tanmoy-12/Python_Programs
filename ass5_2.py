from itertools import permutations 
from itertools import combinations
n=int(input("Enter the number of items in the list : "))
l1=[0 for _ in range(n)]
for i in range(n):
    l1[i] = int(input("Enter number : "))
perms=permutations(l1)
print("The permutations are : \n")
for i in list(perms):
    print(i)
print("\n")
print("The combinations are : \n")
for i in range(1,n+1):
    combs=combinations(l1,i)
    for i in list(combs):
        print(i)