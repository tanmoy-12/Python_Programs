def bubbleSort(l1):
    n = len(l1)
    for i in range(n-1):
        for j in range(n-1-i):
            if l1[j] > l1[j+1]:
                l1[j], l1[j+1] = l1[j+1], l1[j]
    return l1

n = int(input("Enter the number of elements: "))
l1=[]
for i in range(n):
    l1.append(int(input(f"Enter element {i+1}: ")))

sorted_list = bubbleSort(l1)

print("Sorted list in ascending order:")
for i in sorted_list:
    print(i, end=" ")