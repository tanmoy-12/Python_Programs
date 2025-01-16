n = int(input("Ener the number of elements: "))
l1 = []
for i in range(n):
    l1.append(int(input(f"Enter element {i+1}: ")))
max = l1[0]
for i in range(n-1):
    if l1[i+1] > max:
        max = l1[i+1]
max2 = l1[1]
for i in range(n-1):
    if l1[i] > max2 and l1[i]!=max:
        max2 = l1[i]

print(f"Second largest element: {max2}")