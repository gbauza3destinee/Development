


''' Focus on the structure of your functions, let's have fun and learn how they work! :) '''


'''
1. Write as function that converts celsius to fahrenheit
''' 

# def calculate_fahrenheit(temp_celcius):
#   print(f"You input {temp_celcius} degrees celcius\n\nCalculating fahrenheit...\n")
#   fahrenheit = (9/5) * temp_celcius + 32
#   print(f"Fahrenheit temperature: {fahrenheit} degrees")
#   return fahrenheit


# # Here we call the function with our argument
# c = 20 # 20 degrees celcius
# f = calculate_fahrenheit(c)


''' 2. write a function that generates a filename of lastname,
 firstname, and todays date'''

# from datetime import date
# def filename_generate(fname, lname):
#     print(f"{lname}_{fname}_{date.today()}.txt")


# filename_generate("destinee","gonzalez")

'''  3. Function to add two different numbers '''

# def add_two_numbers(a, b):
#   result = a+b
#   print(f'Answer is: {result}')
#   return result

# add_two_numbers(1,2)


'''   4. Function to reverse a word for example 'team' becomes 'maet' '''
def reverse_word(word):
    reversed_word = ""
    for i in word:
        reversed_word = i + reversed_word
    return reversed_word
reverse_word("cat")



'''  5. Function that will deliver the average of 2 values '''





''' 
 6. Write a function that will loop through a string and print whether a character is or is not a vowel.
'''

