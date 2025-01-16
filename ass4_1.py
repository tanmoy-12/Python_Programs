#To create a list of all alphabets
list1=['A' for _ in range(26)]
for i in range(26):
    list1[i]=[chr(i+65) for _ in range(i+1)]
for i in range(26):
    print(list1[i])