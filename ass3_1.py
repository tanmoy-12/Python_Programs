#Reduce a string of lowercase characters in range ascii [‘a’..’z’] by 
# doing a series of operations. In each operation, select a pair of adjacent 
# letters that match, and delete them. Delete as many characters as possible using 
# this method and return the resulting string. If the final string is empty, return Empty String.
def reduce_string(input_string):
    # Initialize an empty list to use as a stack
    reduced_list = []
    
    # Iterate over each character in the input string
    for char in input_string:
        # If the list is not empty and the last character in the list matches the current character
        if len(reduced_list) > 0 and reduced_list[-1] == char:
            reduced_list.pop()  # Remove the matching pair
        else:
            reduced_list.append(char)  # Otherwise, add the current character to the list
    
    # If the list is empty, return "Empty String"
    if len(reduced_list) == 0:
        return "Empty String"
    
    # Join the remaining characters in the list to form the resulting string
    return ''.join(reduced_list)

# Test the function
test_string = "aaabccddd"
result = reduce_string(test_string)
print(f"The resulting string after reduction is: '{result}'")
