''' Exercise - Challenge

Write some code that will print a box around a string.

Examples:
User input: hello
*******
*hello*
*******

User input: programming is fun
********************
*programming is fun*
********************
Hint: You will have to use the len() function, string concatenation (+), and string multiplication (*)

'''

# userInput = input("Print your word or phrase")
# print(userInput)

# top_and_bottom_border = userInput.len() * "*"
# print(top_and_bottom_border)
# print("*" + userInput + "*")
# print(top_and_bottom_border)




''' Strings Part 2'''

# Strings are immutable

str_1 = 'BLUE' 

str_1= str_1.lower()


day = '  TUESDAY   ' # Create a new string with no whitespace 

day_version_2 = day.strip()

len(day_version_2) ## they differ because one has been updated and one hasn't
len(day)

'''Indexing, with square brackets'''

word = 'Jasmine'


# Create a variable to capture the first letter of this string
greeting = 'whatssup!'


# Grab the last letter in a variable



# Using the length and bracket notation, access the last letter in the variable below
month = 'February'



# Using bracket notation access the letter x, the letter e, and the letter d 
first_name = 'Alexandra'

middle_of_string= len(first_name)/2
first_name[int(middle_of_string)]
third_pos = middle_of_string-1
# print(first_name[third_pos])
third_last_pos = (len(first_name)-3)
# print(first_name[third_last_pos])

'''Reverse indexing'''
fav_animal = 'Ostrich'



# Using bracket notation and reverse indexing, access the letter g, the letter i, the letter p
fav_season = 'spring'

letter_g= fav_season[-1]
# print(fav_season[letter_g])
middle_pos = len(fav_season)/2
# print(fav_season[middle_pos])


''' Slicing '''
# There are 3 parameters available with indexing with bracket notation [start:stop:step]
fav_food = 'spaghetti'

# print(fav_food[2])

# Using slicing please create a string that accesses 'rica' in 'America'

country = 'America'

country = country[3:7]
# print(country)



# Using slicing please create a string that accesses 'ora' in 'Dora the explorer'
cartoon = 'Dora the explorer'

cartoon = cartoon[1:4]
# print(cartoon)

# Using slicing please create a string that accesses 'explo' in 'Dora the explorer'

cartoon = cartoon[9:]
print(cartoon)

# Using slicing please create a string that accesses 'albo' in 'Rocky Balboa'
boxer = 'Rocky Balboa'

boxer = boxer[8:]


# Let's step through this string 2 characters at a time
superheroine = 'Wonder Woman'


# Lets step through this entire word and skip by 4
word = 'Supercalifragilisticexpialidocious'


'''Slicing in reverse 
Refer to slice image as a guide if needed

'''


'''

D A Y C A R E
0 1 2 3 4 5 6


D   A   Y   C   A   R   E
-7 -6  -5  -4  -3  -2  -1

'''
random_word = 'daycare' 

# Fun with reverse indexing
# print(random_word[1:0:-1]) # a
# print(random_word[2:0:-1]) # ya
# print(random_word[4:0:-1]) # acya
# print(random_word[5:0:-1]) # racya
# print(random_word[6:0:-1]) # eracya
# print(random_word[7:0:-1]) # eracya
# print(random_word[8:0:-1]) # eracya




'''
Write some code to print the second half of a string.
Example:
python
hon
'''



# End Parameter
# print('Hello', end=' ')
# print('World', end='')
# print('!', end='\n')


# Sep Parameter
# print("Today I woke up at ", 8, " am", sep='*')

'''
Get input from the user and store it in a variable called userin.
Then print the user input. The output should follow exactly this format, including the colon and period at the end:
You entered: userin.
Where userin is what you got from the user.
You must format the print statement like this:
print("You entered",userin)
How can you add sep and end keywords to get the exact formatting shown above?
'''


'''
You need to write a script that will generate an email to a customer who has just made a purchase. You have 3 variables:
name, which stores the customer's name as a string
product, which stores the product name as a string
price, which stores the price of the product as a float
Use an f-string to generate an email message with the following text, and print it. Make sure to round the price to 2 decimal places. The email should be one multi-line string.
Dear {name},
Thank you for your purchase of a {product}. Your credit card has been charged ${price}.
We appreciate your business and look forward to serving you again.
Sincerely,
The ABC Company
'''

name = 'Josiah Wilson'
product = 'ABC Sneakers'
price = 74.95343452342





'''
Write some code that takes a string and tells if it is a palindrome (same forwards and backwards).
Hint: Use indexing/slicing and boolean expressions

Examples:
racecar: True
cat: False
'''



"""
Write some code to print the second half of a string
Example: 
python 
hon 
"""

word = "python" 
half = len(word)/2
size = len(word)
print(half)
half_word = word[int(half):size]
print(type(half_word))

print(half_word)


