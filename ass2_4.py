q = int(input("Enter the number of digitsc: "))
l1 = []
for i in range(q):
    l1.append(int(input(f"Enter the {i+1}th digit: ")))
l2 = l1[::-1]
for i in (l2):
    print(i, end=" ")