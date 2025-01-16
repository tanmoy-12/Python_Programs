#Python program to add two numbers
a=int(input("Enter first number : "))
b=int(input("Enter first number : "))
c=a+b
print("The result is ",c)

#Python program to substract two numbers
a=int(input("Enter first number : "))
b=int(input("Enter first number : "))
d=a-b
print("The result is ",d)

#Python program to multiply two numbers
a=int(input("Enter first number : "))
b=int(input("Enter first number : "))
e=a*b
print("The result is ",e)

#Python program to divide two numbers
a=int(input("Enter first number : "))
b=int(input("Enter first number : "))
f=a/b
print("The result is ",f)

#Python program to divide two numbers & output is integer
a=int(input("Enter first number : "))
b=int(input("Enter first number : "))
d=a//b
print("The result is ",d)

# Python program to check whether a number is even or odd
a=int(input("Enter a number : "))
if a%2==0:
    print("Number is Even")
else:
    print("number is odd")

#Python program to find maximum of two numbers
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
if a>b:
    print(a,"is maximum")
else:
    print(b,"is maximum")

#Python program to find minimum of two numbers
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
if a<b:
    print(a,"is minimum")
else:
    print(b,"is minimum")

#Python program to find maximum of three numbers
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
c=int(input("Enter three number : "))
if a>b and a>c:
    print(a,"is maximum")
elif  b>a and b>c:
    print(b,"is maximum")
else:
    print(c,"is maximum")

#Python program to find minimum of three numbers
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
c=int(input("Enter three number : "))
if a<b and a<c:
    print(a,"is minimum")
elif  b<a and b<c:
    print(b,"is minimum")
else:
    print(c,"is minimum")

#Simple calculator to add,substract,divide,multiply
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
op=input("Enter the operator(+,-,*,/) : ")
if op=='+':
    print("Rseult is ",a+b)
elif op=='-':
    print("Result is ",a-b)
elif op=='*':
    print("Result is ",a*b)
elif op=='/':
    print("Result is ",a/b)
else:
    print("Invalid Operator")

#Gradation System
marks=int(input("Enter marks : "))
if marks>=90 and marks<=100:
    print("Grade A")
elif marks>=70 and marks<70:
    print("Grade B")
elif marks>=50 and marks<70:
    print("Grade C")
elif marks>=30 and marks<50:
    print("Grade D")
elif marks>=0 and marks<30:
    print("Fail")
else:
    print("Invalid Marks")

