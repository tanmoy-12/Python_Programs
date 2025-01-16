#Write a Python function to check whether a string is a pangram or not.

def is_pangram(input_string):
    # Convert the input string to lowercase to handle case insensitivity
    input_string = input_string.lower()
    
    # Create a set to keep track of the unique letters found in the string
    found_letters = set()

    # Iterate over each character in the string
    for char in input_string:
        # Check if the character is a letter (between 'a' and 'z')
        if 'a' <= char <= 'z':
            # Add the character to the set
            found_letters.add(char)
    
    # Check if we have found all 26 letters
    return len(found_letters) == 26

# Test the function
test_string = input("Enter the string : ")
if is_pangram(test_string):
    print(f"'{test_string}' is a pangram.")
else:
    print(f"'{test_string}' is not a pangram.")
