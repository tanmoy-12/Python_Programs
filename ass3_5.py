#To check if a string is superascii
inputString=input("Enter a String : ")
length=len(inputString)
b = [0 for i in range(26)]
for i in range(length):
    index = ord(inputString[i]) - 97 + 1
    b[index - 1] += 1
for i in range(len(inputString)):
    index = ord(inputString[i]) - 97 + 1
    if (b[index - 1] != index):
        print("No")
print("Yes")