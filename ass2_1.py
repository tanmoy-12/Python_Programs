items = int(input("Enter no of items to buy : "))
if(items < 10 and items >= 0):
    print("Your Total Cost would be Rs ",(items*120))
elif(items >=10 and items<=99):
    print("Your Total Cost would be Rs ",(items*100))
elif(items >=100):
    print("Your Total Cost would be Rs ",(items*70))
else:
    print("Invalid Input")
