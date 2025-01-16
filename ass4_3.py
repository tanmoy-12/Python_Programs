#To find out the longest string in a list
list1=["Academy","Of","Technology","Abcdefghijklmnop"]
max=list1[0]
for i in range(len(list1)):
    for j in range(len(list1)):
        if len(max)<len(list1[i]):
            max=list1[i]
print(max)
