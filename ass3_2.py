#Write a Python function that accepts a string and calculates the number of uppercase letters and lowercase letters.
inputString=input("Enter the string : ")
upperCase=0
lowerCase=0
for x in range(len(inputString)):
    if(ord(inputString[x])>=65 and ord(inputString[x])<=90):
        upperCase+=1 
    if(ord(inputString[x])>=97 and ord(inputString[x])<=122):
        lowerCase+=1 
print("The number of lowerCase characters is ", lowerCase, "& upperCase is ", upperCase)