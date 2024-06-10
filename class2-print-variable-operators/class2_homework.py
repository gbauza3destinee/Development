
import math
# 1- Write a program to determine the perimeter of a triangle and print out the result
# perimeter = side_one + base + side_two
# User has a triangle with 1 side (6), oneside(7), base(4)
# Comment for Perimeter
side_one = 6
side_two = 7
base = 4

# perimeter = side_one + base + side_two
# print(perimeter)


# 2- Write some code that converts fahrenheit to celsius 
# c= (f-32) * 5/9
# Comment for Fahrenheit
fahrenheit = 59
celsius = ((fahrenheit - 32) * 5/9)
print(celsius)

# 3- Body Mass Index in pounds 
# weight (lbs) / height (in2) x 703
"""
def findBMI(weight, height):
    bmi = (weight/height) *73 
    print(bmi)

def main():
    if __name__ == "__main__":
        weight = 150
        height = 65
        findBMI(weight, height)
"""

# 4- Solve for volume of a cylinder
    # vol = (pie)radius**2
radius = 5
height = 10
pi = math.pi
volume = (pi*(radius**2))*height
print(volume)