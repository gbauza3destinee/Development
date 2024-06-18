'''
Exercise - Valid email
Write some code that takes input from the user and prints whether it's a valid email address. Make sure to sanitize the user input with .strip()
An email address is valid if:
It has a "." at the third-to-last index
It has exactly one "@" symbol, at the fifth-to-last index or earlier
There is at least one character before the "@" symbol
It doesn't have any spaces (doesn't contain " ")
If all these conditions are met, print True. Otherwise, print False.
To do this, use boolean statements on your string.
Test your code on a few inputs to make sure it works!

'''

# Get input 

email = input("Hello, please enter your email:")
# Clean data
email = email.strip()

# print(email)

# Test 1: It has a "." at the third-to-last index
char_at_index = email[-4]
period_found = char_at_index == "."
# print(period_found)

# if char_at_index == ".":
#     print("true")
# else:
#     print("false")

# Test 2: It has exactly one "@" symbol, at the fifth-to-last index or earlier

test_2=  email[-6::-1]

symbol_in_string = "@" in test_2 ## search for something in a string using in
print(symbol_in_string)

# Test 3: There is at least one character before the "@" symbol

# Test 4: It doesn’t have any spaces (doesn’t contain " ")

# Final Test with AND Keyword
