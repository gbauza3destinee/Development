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
    ### destin3! -- valid case
    ### Supper --- no number or alpha

""" 

username = ""
password = ""


user_has_lowercase = False
user_has_numeric = False
user_has_uppercase = False
user_has_no_spaces = False
user_has_special_chars = False
user_has_length = False

pass_has_lowercase = False
pass_has_numeric = False
pass_has_uppercase = False
pass_has_no_spaces = False
pass_has_special_chars = False
pass_has_length = False


''' A List to handle error messages '''
errors = ['Invalid Username format','Invalid password format']

''' Start your while loop '''


while len(username) <= 8 or len(password) <= 8:    ## Test if entry is 8 chars long
    
    ### Detail the instructions in a first message
    # print(" ")
    # print("Enter your information to signup!")
    # print(" ")
    # print("* * * * * * * * * * * * * * * * * * * ")
    # print("----> Enter a username and password")
    # print(" An username/password is valid if it has:")
    # print(" - one special character")
    # print(" - one number") 
    # print(" - an uppercase first letter") 
    # print(" - a length of 8 characters")
    # print(" - no spaces inside of it")
    print( " ")

    
    ## Get your username and password
    username = input("Enter a valid Username: ")
    print("---------------------------------")
    password = input("Enter a valid Password: ")



    
    ## Username must start with a lowercase letter and only contain 
    # letters, numbers, and underscores.

    
    
    ''' Test your username and enforce logic'''
    # for char in username:
    #     if char.isupper():
    #         print("HAS UPPER")
    #         user_has_uppercase = True
    #     if username[0].islower():
    #         print("LOWER FIRST letter")
    #         user_has_lowercase = True
    #     if char.isnumeric():
    #         user_has_numeric = True
    #         print("HAS NUMERIC")
    #     if not char.isalpha():
    #         user_has_special_chars = True
    #         print("SPECIAL CHars")
    #     if not char == " ":
    #         user_has_no_spaces = True
    #         print("not a space")
    #     if len(username) == 8:
    #         user_has_length = True
    #         print("8 chars")
    #     else:
    #         print(errors[0])

    for char in password:
        if char.isupper():
            print("HAS UPPER")
            pass_has_uppercase = True
        if username[0].islower():
            print("LOWER FIRST letter")
            pass_has_lowercase = True
        if char.isnumeric():
            pass_has_numeric = True
            print("HAS NUMERIC")
        if not char.isalpha():
            pass_has_special_chars = True
            print("SPECIAL CHars")
        if not char == " ":
            pass_has_no_spaces = True
            print("not a space")
        if len(username) == 8:
            pass_has_length = True
            print("8 chars")
        else:
            print(errors[1])

    
    

''' If we pass, congratulate the user and immediately ask them to register'''

''' If they input the correct matching info, program complete. If incorrect, 
        send the user all the way back to the beginning of the loop to start from scratch. '''


# Problem: How are we handling login process after successful sign up?
# Solution: With the assumption that after testing, the username and password
#  fulfill requirements, we can reassign these values to more descriptive
# variables that are meant for the sign in and do a final test with a simple if 
# else. Ternary operators are off the table as they cannot be used in a conditional 
# expression.
# Test, push code, test push code, test push code :)


sys_username = ""

if user_has_lowercase == True and user_has_numeric == True and user_has_uppercase == True and user_has_no_spaces == True and user_has_lowercase == True:
    print("Username is valid!")
    print("Congratulations")
    sys_username = username




    # go through loop again to set up password 
    ## I need to then set them as the system password/username
    ## Extra for loop that checks if they're equal











# Problem: How are we testing password requirements?
# Solution(s): At least 8 characters long
#   Contains at least one uppercase letter
#   Contains at least one lowercase letter
#   Contains at least one digit
#   Contains at least one of these characters: !, ?, @, #, $, ^, &, *, _, -
#   Doesn’t contain any spaces
#   -String methods? Regular Expression? Both are acceptable solutions. Regex is more advanced and will save you a few lines of code
# Test, push code, test push code, test push code :)

