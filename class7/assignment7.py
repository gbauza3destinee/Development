
'''
Improve the login system we wrote last class to allow multiple attempts. You’re developing a login system for a website. Write a Python program that checks whether the user has entered the correct username and password. Just like before:
Create two variables called username and password.
Prompt the user to enter their username and password.
Use conditionals and logical operators to check whether the username and password entered by the user match the username and password variables.
As long as the username and password are incorrect, print “Incorrect username or password”, and keep asking the user for their username and password.
If they match, print “Login successful” and end the program.
'''

username , password = " " , " "
system_username, system_password = "admin", "password"


while (system_username != username and system_password!= password):
    print("Incorrect username or password")
    username = input("Enter your username")
    password = input("Enter your password")
print("Login successful")

