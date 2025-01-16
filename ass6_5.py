def bubbleSort(l1):
    n = len(l1)
    for i in range(n-1):
        for j in range(n-1-i):
            if l1[j] > l1[j+1]:
                l1[j], l1[j+1] = l1[j+1], l1[j]
    return l1
def binarySearch(l1,low,high,search):
    n = len(l1)
    mid = (low + high) // 2
    if high >= low:
        if l1[mid] == search:
            return mid
        elif l1[mid] > search:
            return binarySearch(l1, low, mid)
        elif l1[mid] < search:
            return binarySearch(l1, mid, high)
        else:
            return -1
n = int(input("Enter the number of elements : "))
l1 = []
for i in range(n):
    l1.append(int(input(f"Enter number for {i+1}: ")))
l1 = bubbleSort(l1)
searchItem = int(input("Enter element to search : "))
if(binarySearch(l1,0,n-1,searchItem)!=-1):
    print("Element is present at index",binarySearch(l1,0,n-1,searchItem))
else:
    print("Element is not present in array")