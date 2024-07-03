''' More fun while true!

Write a while true loop that will keep asking the day of the week until you type in Monday

'''



''' Lists 

Lists store a group of objects (things).
In a list, we can have any type of object.
Unlike strings, lists are mutable.
This means we can change an individual object in a list using index.
We can also add and remove objects from a list.
We can also use lists in a for loop.
'''

''' In a list, we can have any type of object. '''

i_can_hold_anything = [1, 'cosmos', True, ['blue', 'green', 'red'], {'south', 'east', 5}, {"firstname":'Sonia'}]


''' Unlike strings, lists are mutable. This means we can change an individual object in a list using index.'''

cars = ['honda', 'ford', 'toyota', 'mersedes'] # mersedes is spelled wrong



''' Lets do some more with indexing '''

animals = ['cat', 'dog', 'bird', 'giraffe']


'''
Fun with List methods
append() Adds an element at the end of the list
clear() Removes all the elements from the list
copy() Returns a copy of the list
count() Returns the number of elements with the specified value
extend() Add the elements of a list (or any iterable), to the end of the current list
index() Returns the index of the first element with the specified value
insert() Adds an element at the specified position
pop() Removes the element at the specified position
remove() Removes the first item with the specified value
reverse() Reverses the order of the list
sort() Sorts the list
'''

# append() Adds an element at the end of the list

days = ['sunday', 'monday']


# clear() Removes all the elements from the list
months = ['january', 'february']


# copy() Returns a copy of the list
copy_me = [1, 2, 6]


# count() Returns the number of elements with the specified value
three_cheers = ['hooray', 'hooray', 'hooray']


# extend() Add the elements of a list (or any iterable), to the end of the current list

new_users = ['Sally', 'Mohammad', ]
current_users = ['Ted', 'Brad', 'Charlie']


# index() Returns the index of the first element with the specified value

cartoons = ['bugs bunny', 'minnie mouse', 'daffy duck']


# insert() Adds an element at the specified position

coding_language = 'Python'
other_languages = ['Javascript', 'Java', 'R']


# pop() Removes the element at the specified position

weather = ['sunny', 'rainy', 'mild']


# remove() Removes the first item with the specified value

movies = ['avengers endgame', 'avengers endgame', 'dune', 'frozen']
\

# reverse() Reverses the order of the list
num_list = [1, 2, 3, 4, 5, 6]

# sort() Sorts the list

letters = ['z', 'b',  'f', 'r']


nums = [4, 5, 10, 19.8, 1, 1004]


''' Exercise

Create a for loop that goes through a list and prints each item in the list, along with its index. (Hint: Create a separate counter variable to keep track of the index.)

Example:
planets = ["mercury", "venus", "earth", "mars"]
0: mercury, 1: venus, 2: earth, 3: mars

'''

planets = ["mercury", "venus", "earth", "mars"]


''' Exercise

Write some code that takes one list and creates a second list that has the type for each entry in the list. Hint: Use the type() function and a for loop

Optional:
Make sure you filter out any repeats.

'''

old_list = ['Wednesday','Thursday', 'Friday', True, ['blue', 'green', 'red'], {"First Name": "Michelle"}, 12.23, {'Sunday', 'Monday', 'Tuesday'}, (1, 2, 3, 4, 5)]




'''
Exercise: List of Pets

You want to make a list containing the names of pets. Keep prompting the user for a pet name until they enter "stop". If it's a new pet, add it to the list. If the list already has that pet, don't add it.

'''




'''
Example: Removing Values
You have a list of numbers, but it contains multiple of the number 2. Remove the number 2 until it only appears in the list once.

'''

removing_values = [1, 2, 3, 2, 2, 3, 4, 5, 6, 2, 2, 2, 2, 2, 1, 1, 5, 6, 5]




'''

Exercise: Removing All Duplicates
You have a list storing important data for your company, but it contains some duplicate entries. Go through your list and remove all the duplicates. When you're done, each item should appear in the list exactly once.
Hint: How would you expand our previous example, which removed duplicates of one value, to remove duplicates of all values?
Hint 2: You might want to make a copy of the original list to use as reference. You may want to use more than one loop.

'''


# original list
states = ['alaska', 'alaska', 'alaska', 'alabama', 'alabama', 'new york', 'new york', 'new york']


