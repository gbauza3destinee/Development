''' Conditionals '''

# Let's write a simple conditional that compares 2 values

x= 25
y = 20 

# if( x > y):
#     print(y)

# Let's try a simple example with strings

fname = 'Marty'

# if fname == 'Marty':
#     print("Hello, Mr.Mcfly")

''' Your turn! :)
Write a program that asks you what the temperature is. 
If it is over 60 degrees, the program will give the user
 a print statement saying, 'It's looking like a warm one 
 today' What potential errors may we be expecting and how can we deal with it..
'''
# temperature = input("What temperature is it?")
# temperature = int(temperature)
# if( temperature > 60):
#     print("It's looking like a warm one today")


'''

Write some code that prints “This is odd” if the user inputs an odd number.
(Hint: use an if statement)
Example:
User input: 7
This is odd

Let's work through some possible steps to solve this

Step 1 Get User's Input



Step 2 Evaluate Data and Deliver output via Conditional
 The question is this, how can we figure out if the value is even or odd? Also, looks like we will be working with numbers. Input will always deliver a string, sounds like a job for integer casting!

'''

# number = input("Enter a number")
# number = float(number)
# if number %2 == 1:
#     print(f"{number} is odd")
# elif number %2 ==0:
#     print(f"{number} is even")
# else:
#     print("Unknown")

'''
Elif

Add to your previous code so it prints “This is odd” if the user enters an odd number, and “This is even” if the user enters an even number.
(Hint: add an elif statement)

User input: 8
This is even


'''




'''

Add to your previous code so if the user enters something that isn’t an odd number or an even number, print “Unknown”. Be ready to troubleshoot our datatypes!
(Hint: add an else statement)


User input: 9
This is odd

User input: 9.2
Unknown

'''



'''

Write some code that takes in a string from the user and prints whether the string is a number, if it is a word, or something else.

Examples:
User input: 7
This is a number

User input: abcde
This is a word

User input: 7!ab5
This is something else

'''

# isDigit = input("Enter any character or number")
# if isDigit.isdigit()== True:
#     print("It's a Digit!")
# elif isDigit.isdigit() == False:
#     print("It's a Character!")

''' Chaining Conditionals code results'''

# result - it is hot outside
# temp_f = 75
# if temp_f > 70:
#     print("It is hot outside")
# elif temp_f > 40:
#     print("It's moderate outside")
# else:
#     print("It's cold outside")


# result - evaluated separately and multiple of them could be run
# temp_f = 75
# if temp_f > 70:
#     print("It is hot outside")
# if temp_f > 40:
#     print("It's moderate outside")
# if temp_f <= 40:
#     print("It's cold outside")


# temp_f = 65
# if temp_f > 70:
#     print("It is hot outside")
# if temp_f > 40 and temp_f < 70:
#     print("It's moderate outside")
# if temp_f <=40:
#     print("It's cold outside")



# Logical operators
# and returns true if they are both true
# print(True and True)
# or returns true if either one of them is true
# print(True or False)

# not returns the opposite
# print(not True)


# Order of Operations
# print(True or False and False)     # and has precedence
# print((True or False) and False)   # parentheses change precedence

# print(not False or True)        # not has precedence
# print(not (False or True))      # parentheses change precedence


''' Fun fact about True Values

Anything that isn’t empty, 0, None, or False, is considered True.

'''


# nested conditionals



'''
You’re working on a project to develop a login system for a website. 
The website requires the user to enter a username and password to log in.
Write a Python program that checks whether the user entered the correct username and password.
Create two variables called username and password and set them to any valid string values.
Prompt the user to enter their username and password using the input() function.
Use conditionals and logical operators to check whether the username and password entered by the user match the username and password variables.
If they match, print “Loga
in successful.” If they don’t, print “Incorrect username or password.”

Follow the requirements, nothing more, nothing less. 
'''



# Initialize system values


# Get sign on and pass from user


# Evaluate and Output (using conditionals, boolean operators, and logical operators)

## Take a variable ‘age’ which is of positive value and check the following:
# age = input("Enter your age")
# if age < 10 :
#     print("children")
# elif age > 60:
#     print("senior citizen")
# elif age < 60 and age > 10:
#     print("adult")
## If the age is less than 10, print “Children”.
 
## If the age is more than 60, print ‘senior citizen’
 
## If it is between 10 and 60, print ‘adult’