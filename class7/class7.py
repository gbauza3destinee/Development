
''' While Loops

While loops run as long as the given condition returns a True boolean.

'''


# end = int(input("Enter your number"))
# counter = 0

# while counter <= end : 
#     print(counter)
#     counter+=1

''' Example
Create a while loop that prints every integer from 1 to 10.
'''


# i =0
# while i < 10:
#     print(i)
#     i+=1




''' While loops and user input 

This will keep asking us to input a word until we input "stop" Let's follow it line by line

'''

# userInput = " "

# while(userInput != "stop"):
#     userInput = input("Enter something")
#     userInput.lower()
#     print(userInput)



'''
Improve the login system we wrote last class to allow multiple attempts. You’re developing a login system for a website. Write a Python program that checks whether the user has entered the correct username and password. Just like before:
Create two variables called username and password.
Prompt the user to enter their username and password.
Use conditionals and logical operators to check whether the username and password entered by the user match the username and password variables.
As long as the username and password are incorrect, print “Incorrect username or password”, and keep asking the user for their username and password.
If they match, print “Login successful” and end the program.
'''


# username , password = " " , " "
# system_username, system_password = "admin", "password"


# while (system_username != username and system_password!= password):
#     print("Incorrect username or password")
#     username = input("Enter your username")
#     password = input("Enter your password")
# print("Login successful")




''' For Loops
For loops are used to iterate through something.
For loops perform an action on a group of objects
For loops can be performed on iterables: 

Strings
Lists
Tuples
Dictionaries
Sets

# The Temporary Variable (item, goes out of scope after for loop ends)
for item in collection:
	print(item)

'''

'''
Lets loop through the string "Hello World"

# '''
# my_string = "hello world"
# for c in my_string:
#     print(c)




'''
Lets loop through a list of colors

'''
# my_colors = ['red', 'green', 'orange', 'yellow']

# for color in my_colors: 
#     print(color)

'''Lets loop through a tuple

'''
my_fav_food = ('pizza', 'subs', 'chicken')

# for food in my_fav_food:
#     print(food)


'''
Example
Write a for loop that loops through a string, counts all the letters, and then print how long the string is.

# '''

# string = "character"
# counter = 0
# for c in string : 
#     print(counter)
#     counter +=1




'''
Exercise - Lets try to add conditionals to the mix

Take a string from the user. Verify that it’s a number.
Write a for loop that adds all the digits together. Then print the total.

Example:
'14253'
15

Hint: remember to cast to int() for each digit in the loop

'''



# # initialize variables and get user input3
# user = int(input("Enter a number"))



# # # Verify Decimal, if it is, lets do our fun loop, else we will send the user home with a nice message
# isNumber = user.isdigit

# total = 0
# if( isNumber == True): 
#     for num in user:
#         total+=num
# elif(isNumber == False):
#     print("Not a number sorry")
    

''' More conditionals in loops'''




''' Cleaning Strings

You’re working on a data analysis project for a company that looks at written text. 
You’re only interested in letters from A-Z because you’re analyzing language. 
However, the data you’re given has some values that shouldn’t be there.
Write a Python program that takes a string as input from the user, removes anything 
from the string that isn’t a letter, and prints the new string.
You can loop through the string in a for loop, use the .isalpha() string method, 
and remember that strings are immutable, so you will have to build a new string from 
scratch using string concatenation.

test_string = 'a56b32ra87ca++d#@a*&b21r23a'

'''


userin = input("Insert string")
word_2 = ""
for i in userin:
    if i.isalpha():
        word_2 += i
    else:
        continue

print(word_2)
