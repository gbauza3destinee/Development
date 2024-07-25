from statistics import mean 

"""
Write a function that takes a list of numbers as 
input and returns the average of all the numbers 
in that list. Have fun and be sure to test test test! 
"""
## Test result 
num_list = [1,3,4,5,6]
print("Mean should be " + mean(num_list))

## Define a method
def find_average(num_list):
    result = 0
    for n in num_list:
        result += n

    result = result / len(num_list)
    print("Actual Mean: " + result)
    return result


find_average(num_list)