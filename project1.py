### Debugging:
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
spaces = " "
special_characters = "!?@#$^&,*_-"
numbers = "0123456789"
lowercase_letter = "abcdefghijklmnopqrstuvwxyz"
uppercase_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
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


    ### Check if username/password is upper, contains special chars and numbers
    if not username in special_characters or not username in numbers or not username in uppercase_letter or not username in lowercase_letter:
        print("Username does contain number" , username in numbers)
        print("Username does contain special chars" , username in special_characters)
        print("Username does have letter as upper char" , username in uppercase_letter)
        print("Username does have letter as lower char", username in lowercase_letter)
        print(errors[0])
    if not password in special_characters or not password in numbers or not password in uppercase_letter or not password in lowercase_letter:
        print("Password does contain number" , password in numbers)
        print("Password does contain special chars" , password in special_characters)
        print("Password does have letter as upper char" , password in uppercase_letter)
        print("Password does have letter as lower char", password in lowercase_letter)
       
        print(errors[1])

    ## Check if username or password contains a length of 8 
    if not len(username) == 8:
        print("Invalid - Username length not 8")
        errors[0]
    if not len(password) == 8:
        print("Invalid - Password length not 8")
        errors[1]
    ## Check if username or password contains  spaces
    if username in spaces or password in spaces:
       print("Cannot contain spaces")

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
