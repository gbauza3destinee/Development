### Debugging:

## make lists into variables


## My not in statements don't seem to be working
##  With the case "destin6*" which has nums and special chars
##  result is False: contains number False: contains char
##  False: for lowercase and uppercase
##  tried: changing not in nums to not .isnumeric and same response.


''' Initialize your variables 

We will need 2 variables to capture the username and password. 
Another 2 variables to use as the system username and password 
to authenticate against when we register
'''

"""  Test cases 
    ### destin6* -- no upper
    ### Destine@ -- no number
    ### Destin45 -- no special char
    ### Des in4& -- contains space
    ### Des3!    -- not 8 chars
    ### Destin3! -- valid case

""" 

username = ""
password = ""


user_has_lowercase = False
user_has_numeric = False
user_has_uppercase = False
user_has_spaces = False

pass_has_lowercase = False
pass_has_numeric = False
pass_has_uppercase = False
pass_has_spaces = False


''' A List to handle error messages '''
errors = ['Invalid Username format','Invalid password format']

''' Start your while loop '''



while len(username) <= 8 or len(password) <= 8:    ## Test if entry is 8 chars long
    
    ### Detail the instructions in a first message
    print(" ")
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


    ### Check if username/password is upper, contains special chars, spaces and numbers

    for char in username:
        if char.isupper():
            user_has_uppercase = True
        elif char.islower():
            user_has_lowercase = True
        elif char.isnumeric():
            print("Username does contain number" , char.isnumeric())
            user_has_numeric = True
        elif not char.isalnum():
            print("Username does contain special chars", not char.isalnum())
            user_has_special_char = True

    for char in password:
        if char.isupper():
            pass_has_uppercase = True
        elif char.islower():
            pass_has_lowercase = True
        elif char.isnumeric():
            print("Username does contain number" , char.isnumeric())
            pass_has_numeric = True
        elif not char.isalnum():
            print("Username does contain special chars", not char.isalnum())
            pass_has_special_char = True
        elif not char == " ":
            print("Does not contain spaces")
            pass_has_spaces = True
    
    ## Check if username or password contains a length of 8 
    if not len(username) == 8:
        print("Invalid - Username length not 8")
        errors[0]
    if not len(password) == 8:
        print("Invalid - Password length not 8")
        errors[1]
   

    ### HAPPYCASE:


    if user_has_lowercase == True and user_has_numeric == True and user_has_uppercase == True and user_has_spaces == True and pass_has_lowercase == True and pass_has_numeric == True and pass_has_uppercase and pass_has_special_char == True:
        print("Username is valid!")


    # go through loop again to set up password 
    ## I need to then set them as the system password/username
    ## Extra for loop that checks if they're equal


    ''' If we pass, congratulate the user and immediately ask them to register'''
    if username in uppercase_letter and username in lowercase_letter and username in special_characters and len(username) == 8 and username not in spaces:
        print("Username is valid!")
        print(" ---- Congratulations, User and Password saved.")
        register_confirmation = input("Register? Y for Yes, and N for no")

        ''' If they input the correct matching info, program complete. If incorrect, 
        send the user all the way back to the beginning of the loop to start from scratch. '''

        if register_confirmation == "Y": 
            print("Program complete: User and Password saved.")
        else : 
            print("Program complete: User not registered.")
        break










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
