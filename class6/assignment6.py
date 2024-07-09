'''
You’re working on a project to develop a login system for a website. 
The website requires the user to enter a username and password to log in.
Write a Python program that checks whether the user entered the correct username and password.
Create two variables called username and password and set them to any valid string values.
Prompt the user to enter their username and password using the input() function.
Use conditionals and logical operators to check whether the username and password entered by the user match the username and password variables.
If they match, print “Login successful.” If they don’t, print “Incorrect username or password.”

Follow the requirements, nothing more, nothing less. 
'''
# Get user sign on values
username = input("Enter a username: ")
password = input("Enter a password: ")

#Set values for username and password
hardcoded_username = 'user123'
hardcoded_pwd = 'password123' 

#Conditionals 
if username == hardcoded_username and password == hardcoded_pwd:
    print("Correct username and password!")
    print("Log in successful!")
elif username == hardcoded_username and password!= hardcoded_pwd:
    print("Incorrect password!")
else :
    print("Incorrect username or password!")
