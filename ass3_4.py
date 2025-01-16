#To check if a string is palindrome or not
inputString=input("Enter a String : ")
if inputString == inputString[::-1]:
    print("Palindrome String")
else:
    print("Not Palindrome")