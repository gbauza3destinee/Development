
''' Initialize your variables 

We will need 2 variables to capture the username and password. 
Another 2 variables to use as the system username and password 
to authenticate against when we register
'''
username = ""
password = ""
special_characters = "!?@#$^&,*_-"
numbers = "0123456789"
''' A List to handle error messages '''
errors = ['!!!Invalid Username!!!','!!!Invalid password format!!!']

''' Start your while loop '''

while len(username) <= 8 or len(password) <= 8:    ## Test if entry is 8 chars long
    
    ### Detail the instructions in a first message
    print("Enter your information to signup!")
    print(" ")
    print("* * * * * * * * * * * * * * * * * * * ")
    print("----> Enter a username and password")
    print(" An username/password is valid if it has:")
    print(" - one special character")
    print(" - one number") 
    print(" - an uppercase first letter") 
    print(" - a length of 8 characters")
    print(" - no spaces inside of it")
    print( " ")

    
    ## Get your username and password
    username = input("Enter a valid Username: ")
    print("---------------------------------")
    password = input("Enter a valid Password: ")

    ### Test cases 
    ### destin6* -- no upper
    ### Destine@ -- no number
    ### Destin45 -- no special char
    ### Des in4& -- contains space

    ### Check if is upper, contains special chars and numbers
    if not username in special_characters or not username in numbers or not username[0].isupper():
        print(errors[0])
    if not password in special_characters or not password in numbers or not password[0].isupper():
        print(errors[1])

    ## Check if length is 8 
    if not len(username) == 8:
        print("Invalid - Length not 8")
        errors[0]
    if not len(password) == 8:
        print("Invalid - Length not 8")
        errors[1]

    ## Check if contains spaces 
    for char in username:
        if char == " ":
            print("Cannot contain spaces")
            print(errors[0])
  











    


''' If we pass, congratulate the user and immediately ask them to register'''




''' If they input the correct matching info, program complete. If incorrect, send the user all the way back to the beginning of the loop to start from scratch. '''




# Problem: How are we testing password requirements?
# Solution(s): At least 8 characters long
#   Contains at least one uppercase letter
#   Contains at least one lowercase letter
#   Contains at least one digit
#   Contains at least one of these characters: !, ?, @, #, $, ^, &, *, _, -
#   Doesn’t contain any spaces
#   -String methods? Regular Expression? Both are acceptable solutions. Regex is more advanced and will save you a few lines of code
# Test, push code, test push code, test push code :)


# Problem: How are we handling login process after successful sign up?
# Solution: With the assumption that after testing, the username and password fulfill requirements, we can reassign these values to more descriptive variables that are meant for the sign in and do a final test with a simple if else. Ternary operators are off the table as they cannot be used in a conditional expression.
# Test, push code, test push code, test push code :)
