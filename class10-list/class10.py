'''
Ranges
    - Must be integers, whole numbers
    - Used to iterate
    - Does not store all the numbers, but knows what they should be
    - Simple to write and create
    -saves memory

    If you need a range of a specific number make sure to count up +1 
'''

# Using the range function, lets count to 20

twenty_one  = range(21)

# for n in twenty_one:
#     print(n)



''' Let's try these '''




'''
Write a range that is every five years from 1960 to 2000.
'''

'''
range(start, stop, step)
'''

five_year = range(1960, 2001, 5)




'''
Write a range that counts down from 30 to 0
'''
countdown = range(30,-1, -1)





'''
Exercise
Rewrite the for loop we made last class that goes
 through a list and prints each item in the list, along 
 with its index. (Hint: you can use a range, and you won't
   need a separate counter variable.)

Example:
planets = ["mercury", "venus", "earth", "mars"]
0: mercury, 1: venus, 2: earth, 3: mars
'''

planets = ["mercury", "venus", "earth", "mars"]
output = ''

# for i in range(len(planets)) : 
#     print(str(i) + " " + planets[i])




''' Exercise
You have a list of employees, and a list of job titles. 
Assume the lists are the same length and in the same order.
Use one for loop to go through both lists and print the 
job title of each employee.
For example, if these are your lists:
employees = ['Bob', 'Cynthia', 'Abdul']
job_titles = ['accountant', 'engineer', 'recruiter']
This should be your output:
Bob's job title is accountant.
Cynthia's job title is engineer.
Abdul's job title is recruiter.

'''


employees = ['Bob', 'Cynthia', 'Abdul']
job_titles = ['accountant', 'engineer', 'recruiter']

# for i in range(len(employees)):
#     print(employees[i]+ "'s job title is " + job_titles[i])


'''
Write some code that creates a range based on what the user enters. 
Challenge: you can make a range with 1, 2, or 3 numbers. 
How would you allow the user to pick any of these options?
'''

while True:
 
 
    choice = input("Choose 1, 2, or 3 parameters for your range: ")
 
 
    if choice == '1':
        start_1 = int(input("How long is your range: "))
        output_1 = range(start_1)
        for o in output_1:
            print(o, end=' ')
        break
 
    if choice == '2':
        start_2 = int(input("How long is start value: "))
        stop_2 = int(input('What is your stop value: '))
        output_2 = range(start_2, stop_2)
        for o in output_2:
            print(o, end=' ')
        break
 