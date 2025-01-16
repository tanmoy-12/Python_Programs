#To add elements of two list
n=int(input("Enter the size of list : "))
list1 = [0 for _ in range(n)]
list2 = [0 for _ in range(n)]
for i in range(n):
    list1[i]=int(input("Enter the value for list 1 : "))
print("\n")
for i in range(n):
    list2[i]=int(input("Enter the value for list 2 : "))
for i in range(n):
    list1[i]+=list2[i]
print("\nThe output list is ")
print(list1)