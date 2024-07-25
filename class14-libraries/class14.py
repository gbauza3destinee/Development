## pip install <package>
## https://docs.python.org/3/py-modindex.html


'''
Example
Import the math library.
Take the radius of a circle as user input.
Then, compute the area of the circle using the math library.

The equation for area of a circle is pi * radius * radius
'''

import math 
# radius = int(input("Enter your radius"))
# area_of_a_circle = math.pi * radius * radius 
# print(area_of_a_circle)



'''
Exercise
Lets make some magic happen with the statistics library.
'''
 # for median, mode, average
import statistics 

# With Statistics Library

# middle value in odd numbered list
odd_list = [1, 2, 3, 4, 5, 2, 9, 1, 3, 4, 6, 7]
odd_list.sort()

median_of_an_odd_list = statistics.median(odd_list)

# average of two middle values
even_list = [1, 2, 3, 4, 5, 2, 9, 1, 3, 4, 6, 7]
median_of_an_even_list = statistics.median(even_list)

'''
Exercise
Lets make some magic happen with the pandas library. But before we do that, let's use the OS library to make sure everything generates in our current directory
'''


import pandas as pd
import os 
## grabbing the location of this file.
os.chdir(os.path.dirname(os.path.abspath(__file__)))
 
# __file__ is a built-in constant containing the pathname of the file from which the running Python module was loaded. 

# os.path.abspath to return the directory name of the path which we have provided as the argument of the function.

# os.path.dirname returns the directory name of the path

# os.chdir changes the current working directory to a specific path

# dictionary with my users
users = {
  "acct_num": ['abb', 'cde', 'ggh', 'sdf'],
  "name": ['jim', 'sarah', 'tanya', 'bob']
}


# load into a dataframe
df = pd.DataFrame(users)
# print(df)
# generate a csv in our current working directory
df.to_csv("testing.csv", index = False)


'''
Exercise
Lets make some magic happen with the date time library.
'''

from datetime import date 

today = date.today()

# print(f"This month is {today.month}")
# print(f"This day is {today.day}")



'''
https://jsonplaceholder.typicode.com/

This website provides free api testing. Lets leverage python's request module to see if we can do a get request against this data
'''
import requests 

my_response = requests.get('https://jsonplaceholder.typicode.com/')
# print(my_response.text)


''' Oooh Fun with Tkinter

Source: https://www.tutorialspoint.com/taking-input-from-the-user-in-tkinter

'''

# # #Import the required Libraries
# from tkinter import *
# from tkinter import ttk

# # #Create an instance of Tkinter frame
# win= Tk()

# # #Set the geometry of Tkinter frame
# win.geometry("750x250")

# def display_text():
#    global entry
#    string= entry.get()
#    label.configure(text=string)

# # #Initialize a Label to display the User Input
# label=Label(win, text="", font=("Courier 22 bold"))
# label.pack()

# # #Create an Entry widget to accept User Input
# entry= Entry(win, width= 40)
# entry.focus_set()
# entry.pack()

# # #Create a Button to validate Entry Widget
# ttk.Button(win, text= "Okay",width= 20, command= display_text).pack(pady=20)

# win.mainloop()







'''
Generate PDF for Dual Employment Signature
'''

# Generate pdf file in same directory as Python file
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# Dictionary will capture the variables and data we want to have on the pretty pdf
pdf_variables = {} ## create a dictionary from scratch
# Lets get the name and fav colors for our PDF! 

first_name = input("What is your first name? ").title()
fav_color = input("What is your favorite color? ").title()
 
 ## add values to dictionary
 
pdf_variables.update({"firstname": first_name, "fav_color":fav_color})
 
print(pdf_variables)

pdf_template = '''
<p style="text-align: center;"><strong> Hi, {{firstname}}, your favorite color is {{fav_color}}</strong></p>
'''

import os 
from jinja2 import Template
from pyhtml2pdf import converter

# Formatted html for final output

Func = open("name_and_color.html", "w")
Func.write(final_pdf.render(pdf_variables))
# To PDF
path = os.path.abspath('name_and_color.html')
converter.convert(f'file:///{path}', f'{first_name.lower()}.{fav_color.lower()}.pdf')
 
# Cleanup
os.remove("name_and_color.html")



''' Last Exercise - Pick a library not on this list and read the documentation, try it out, have fun with it!'''