def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)
def factorial_nonrecursive(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
n = int(input("Enter the number : "))

# Recursive factorial
print("The factorial of {n} is ",factorial_recursive(n))

# Non-recursive factorial
print("The factorial of {n} is ",factorial_nonrecursive(n))