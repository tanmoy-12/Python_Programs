#To apply CustomCaesarCipher encryption
def CustomCaesarCipher(key, message):
    message=list(message)
    length=len(message)
    for i in range(length):
        index=0
        if '0'<= message[i] <='9' or 'a'<= message[i] <='z' or 'A'<= message[i] <='Z':
            index=ord(message[i])
            index+=key
            message[i]=chr(index)
    return ''.join(message)
inputString=input("Enter a String : ")
key=int(input("Enter the key : "))
if key==0:
    print("INVALID INPUT")
else:
    print("Encrypted string is "+ CustomCaesarCipher(key,inputString))