''' More fun while true!

Write a while true loop that will keep asking
 the day of the week until you type in Monday

'''

# while True: 
#     day = input("Enter day of week ")

#     if (day == "Monday") : 
#         break
#     else : 
#         continue

''' Lists 
.append()
.pop() remove last element
.remove() remove specific element 
.sort() o log n - tim sort

Trick for removing duplicates from a list
no_repeats = list(set(new_list))


Lists store a group of objects (things).
In a list, we can have any type of object.
Unlike strings, lists are mutable.
This means we can change an individual object in a list using index.
We can also add and remove objects from a list.
We can also use lists in a for loop.
'''

''' In a list, we can have any type of object. '''


i_can_hold_anything = [1, 'cosmos', True, ['blue', 'green', 'red'], {'south', 'east', 5}, {"firstname":'Sonia'}]


''' Unlike strings, lists are mutable. 
This means we can change an individual 
object in a list using index.'''

cars = ['honda', 'ford', 'toyota', 'mersedes'] # mersedes is spelled wrong



''' Lets do some more with indexing '''

animals = ['cat', 'dog', 'bird', 'giraffe']
# cat = animals[0]
# print(cat)
# tiger = animals[1]

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

# days.append('tuesday')


# clear() Removes all the elements from the list
months = ['january', 'february']

# months.clear()

# copy() Returns a copy of the list
copy_me = [1, 2, 6]

# copy_2 = copy_me.copy()

# count() Returns the number of elements with the specified value
three_cheers = ['hooray', 'hooray', 'hooray']

# three_cheers.count("hooray")


# extend() Add the elements of a list (or any iterable), to the end of the current list

new_users = ['Sally', 'Mohammad']
current_users = ['Ted', 'Brad', 'Charlie']

# new_users.extend(current_users)

# index() Returns the index of the first element with the specified value

cartoons = ['bugs bunny', 'minnie mouse', 'daffy duck']
# index_of_minnie = cartoons.index("minnie mouse")

# insert() Adds an element at the specified position

coding_language = 'Python'
other_languages = ['Javascript', 'Java', 'R']

other_languages.insert(1, coding_language)
# pop() Removes the element at the specified position

weather = ['sunny', 'rainy', 'mild']
# weather.pop(1)

# remove() Removes the first item with the specified value

movies = ['avengers endgame', 'avengers endgame', 'dune', 'frozen']

# movies.remove("avengers endgame")
# print(movies)

# reverse() Reverses the order of the list
num_list = [1, 2, 3, 4, 5, 6]

# print(num_list.reverse())

# sort() Sorts the list O LOG N

nums = [4, 5, 10, 19.8, 1, 1004]
# nums.sort()

## Sorted returns a new list

letters = ['z', 'b',  'f', 'r']

# new_letters = sorted(letters)





''' Exercise

Create a for loop that goes through a list and prints
 each item in the list, along with its index. (Hint: 
 Create a separate counter variable to keep track of the index.)

Example:
planets = ["mercury", "venus", "earth", "mars"]
0: mercury, 1: venus, 2: earth, 3: mars



'''
    
planets = ["mercury", "venus", "earth", "mars"]

# for planet in planets:
#     index_of_planet = planets.index(planet)
#     print(index_of_planet , " : " , planet)


''' Exercise

Write some code that takes one list and creates a second 
list that has the type for each entry in the list. Hint: 
Use the type() function and a for loop

Optional:
Make sure you filter out any repeats.

'''

# old_list = ['Wednesday','Thursday', 'Friday', True,
#              ['blue', 'green', 'red'], {"First Name": "Michelle"}, 
#              12.23, {'Sunday', 'Monday', 'Tuesday'}, (1, 2, 3, 4, 5)]
# new_list = []

# for element in old_list:
#     type_of_element = type(element)
#     new_list.append(type_of_element)

# no_repeats = list(set(new_list))
# print(no_repeats)
'''
Exercise: List of Pets

You want to make a list containing the names of pets. 
Keep prompting the user for a pet name until they enter 
"stop". If it's a new pet, add it to the list. If the list 
already has that pet, don't add it.

'''
# pet_list = []
# while True: 
#     pet = input("Enter the name of your pet")

#     if pet == "stop":
#         print(pet_list)
#         break
#     elif pet in pet_list : 
#         continue
#     else: 
#         pet_list.append(pet)

'''
Example: Removing Values
You have a list of numbers, 
but it contains multiple of the number 2.
 Remove the number 2 until it only appears in the list once.

'''

# removing_values1 = [1, 2, 3, 2, 2, 3, 4, 5, 6, 2, 2, 2, 2, 2, 1, 1, 5, 6, 5]


# for n in removing_values1: 
#     if removing_values1.count(2) > 1:
#         removing_values1.remove(2)

# print(removing_values1)


'''

Exercise: Removing All Duplicates
You have a list storing important data for your company, 
but it contains some duplicate entries. Go through your list and 
remove all the duplicates. When you're done, each item should appear 
in the list exactly once.
Hint: How would you expand our previous example, which removed
 duplicates of one value, to remove duplicates of all values?
Hint 2: You might want to make a copy of the original list to 
use as reference. You may want to use more than one loop.

'''


# original list
states = ['alaska', 'alaska', 'alaska', 'alabama', 'alabama', 'new york', 'new york', 'new york']

unique_states = list()

# for state in states :
#     if state not in unique_states:
#         unique_states.append(state)

# # print(unique_states)
        

states3 = list(set(states))
print(states3)
