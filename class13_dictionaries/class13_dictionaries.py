

''' Fun facts about dictionaries 

    -collection of keys and values
    -used to store associated information
    -keys are the words, values are the definitions

'''

# How do we create a dictionary?

user_data = {"user_id": 400,
           "fname": "Fritz"}




# Dictionary will capture the variables and data 
pdf_variables = {} ## create a dictionary from scratch
# Lets get the name and fav colors for our PDF! 

first_name = input("What is your first name? ").title()
fav_color = input("What is your favorite color? ").title()
 
 ## add values to dictionary
 
pdf_variables.update({"firstname": first_name, "fav_color":fav_color})
 
print(pdf_variables)


# Bracket notation - we can grab the value by referencing the key

# print(user_data["fname"])
# print(user_data["user_id"])

# # Add new key/value pair

user_data["address"] = "elm street"
# print(user_data)


# lets look at all the methods available to us
# print(dir(user_data))

# lets try one 
# print(user_data.__contains__("userid")) ## checks if a key is contained in dictionary

# Dict constructor
new_dict = dict()
# print(type(new_dict))

# Let's update our name key
# user_data = dict(user_id: 400, fname : "daisy")


# Dictionary methods
# Lets use the keys methods to get the keys from this dictionary

dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}

# Let's look at our keys
dog_information = dog.keys()


# Lets use the values methods to get the values from this dictionary

dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}

# Lets look at our values
dog_values = dog.values()

# print(dog_values)

# Lets use clear method to remove all elements

dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}

dog.clear()

# Lets use get method to get a key value

dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}



# lets look at one of the parameters to show an error if the key doesnt exist



# Lets create a copy

dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}

new_dog = dog.copy()
dog['breed'] = "Golden Retriever"

# print(f"Original Dictionary: {dog}")
# print(f"Copy of original{new_dog}")



# Lets remove a specified key with pop
dog = {
    "breed": "japanese chin",
    "gender": "male",
    "age": 7
}

## takes name of key
dog.pop("gender")
# print(dog)


# Lets remove a last inserted key-value pair with popitem
dog = {
    "breed": "japanese chin",
    "gender": "male",
    "age": 7
}

age = dog.popitem()
# print(age)

# Get a list with each key-value pair with items
dog = {
    "breed": "japanese chin",
    "gender": "male",
    "age": 7
}

list1 = dog.items()
# print(list1)
    

# we can loop through
dog = {
    "breed": "japanese chin",
    "gender": "male",
    "age": 7
}

# for k, v in dog.items(): 
#     print(k, v) 


# Update dictionary
dog = {
    "breed": "japanese chin",
    "gender": "male",
    "age": 7
}

dog.update({"temperament": "happy"}) ## let's you add in a KV entry or update current
size = {"size" : "small"} ## also another way to add a KV entry
# print(dog)

# Update can also update current key value pairs, as well as adding
dog.update({"size": "small"})


# Dictionaries vs Lists
# list1 = ['a', 'b', 'c', 'd', 'e']
# dict1 = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 5: 'e'}





'''
Write some code that takes two lists and converts them into one dictionary.
In:
list1 = ['one', 'two', 'three']
list2 = [4, 10, 30]
Out:
{'one': 4, 'two': 10, 'three': 30}

'''

list1 = ['one', 'two', 'three']
list2 = [4, 10, 30]
new_dict = {}
 
for i in range(len(list1)):
    new_dict.update({list1[i] :list2[i]})
# print(new_dict)


''' Zip Solution

When you use the zip() function in Python, 
it takes two or more data sets and "zips" them together. 
This returns an object containing pairs of items derived 
from the data sets. 
'''

my_keys = ['one', 'two', 'three']
my_values = [4, 10, 30]

result = dict(zip(my_keys, my_values))
# print(result)


'''
Exercise

Write a dictionary with five countries and their languages 
Then have your code print the languages of each country one at a time.
Hint: Use the items() method


'''

languages = { 'USA': 'English', 'Mexico': 'Spanish', 'France': 'French', 'Portugal':'Portugese', 'Belgium':'Dutch' }

# for key, value in languages.items():
#     print(f"Language is {key} of country {value}")



# As datasets, we can use bracket notation

choices = {"flavors":['strawberry', 'vanilla', 'orange'],
           "sizes":['large', 'medium', 'small'],
           "region":['south america', 'central asia', 'united states']}

# print(choices["flavors"][1])
# print(choices["size"][2])

import pandas as pd
# Lets make a dataframe out of this
choices_df = pd.DataFrame(choices)
# print(choices_df)

# Lets rename the columns
rename_choices_dict = {"flavors": "column1",
                       "sizes": "column2",
                       "region" : "column3"}

choices_df.rename(columns=rename_choices_dict, inplace = True)
# print(choices_df)
choices_df.to_csv('output.csv', index = False) ## output to csv file


'''
Exercise
Create a dictionary for an automobile including make, model, year, number of doors, and number of cylinders.
'''


'''
In statistics, the mode is the value that appears most frequently in a dataset.
For example, in this list: [1,2,4,1,3,4,1,1] the mode is 1
Write some code that uses a dictionary to calculate the mode of a list.

'''

my_list_items = [1,2,4,1,3,4,1,1] # our list

output = {}
for m in my_list_items:
    if m not in output:
        output[m] = 1
        # print(output)
    else: 
        output[m]+=1
print(output)


# What about the count method for Lists?? 
for m in my_list_items :
    output[m] = my_list_items.count(m)

# from statistics import mode
from statistics import mode
result  = mode(my_list_items)
print(result)

'''
Suppose you have a list of employee records that contain the following information for each employee: name, job title, salary. The records are stored as a list of dictionaries.
Use this list to create a dictionary where the keys are the job titles and the values are the average salaries for each job title.
Example:
records = [{'name': 'Bob', 'title': 'manager', 'salary': 50000},\
           {'name': 'Alice', 'title': 'developer', 'salary': 60000},\
           {'name': 'David', 'title': 'developer', 'salary': 65000}]
Output: {'manager': 50000, 'developer': 62500}
'''

records = [{'name': 'Bob', 'title': 'manager', 'salary': 50000},
           {'name': 'Alice', 'title': 'developer', 'salary': 60000},
           {'name': 'David', 'title': 'developer', 'salary': 65000}]


# our output dictionaries
title_salary_dict = {} # capture our titles and salary totals
title_count_dict = {} # capture title count


for r in records:
    # print(r) # each loop through will show us a dictionary
    title = r['title']
    salary = r['salary']
    # print(title)
    # print(salary)
    if title not in title_salary_dict:
        title_salary_dict[title] = salary
        title_count_dict[title] = 1
        # print(title_salary_dict)
        # print(title_count_dict)
    else:
        title_salary_dict[title] += salary
        title_count_dict[title] += 1
        
# print('all titles and sum of salaries', title_salary_dict)
# print('titles and employee count', title_count_dict)

result = {s:float(title_salary_dict[s])/title_count_dict[s] for s in title_salary_dict}
# print(result)



import pandas as pd

records = [{'name': 'Bob', 'title': 'managers', 'salary': 50000},
           {'name': 'Alice', 'title': 'intern', 'salary': 60000},
           {'name': 'David', 'title': 'intern', 'salary': 65000},
           {'name': 'Des', 'title': 'developer', 'salary': 165000},
           {'name': 'Sarah', 'title': 'managers', 'salary': 165000}]

df = pd.DataFrame.from_records(records) # building the dataframe from our list of dictionaries

result = df.groupby('title')['salary'].mean()
# print(result)

# how we loop through a pandas dataframe
for key, value in df.iterrows():
    print(key, value)
















 



