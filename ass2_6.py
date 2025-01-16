# Print the pyramid in inverted format
n = int(input("Enter the total number of rows: "))
for i in range(n):
    # Print leading spaces
    for k in range(i):
        print(" ", end='')
    # Print stars
    for j in range(2 * (n - i) - 1):
        print("*", end='')
    print("")
