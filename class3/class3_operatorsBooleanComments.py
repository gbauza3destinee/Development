# Operators, Boolean Expressions and Comments

# I am a single line comment 
temperature = 95 #I am an inline comment 
first_name = "Destinee" """
Hello this is an inline multi-line comment! """

#Comment 
length = 5 # length of the rectangle
width = 7 # width of the rectangle 
perimeter = 2 * (length + width) #calculating the perimeter of rectangle
# print(perimeter) 

""" Converts a fahrenheit temperature 
to a celsius temperature
Using an equation """

fahrenheit = 90
celsius = (fahrenheit - 32) * 5/9
# print(celsius)

""" Shortcut Operators """
#Add 5 to me 
age = 25
age += 5
# print(age)

# Add 10 years to 2024
year = 2024
year+=10
# print(year)

#Subtract 20
num_one = 55
num_one -=20
# print(num_one)

#Subtract 15
num_two = 11
num_two -= 15
# print(num_two)

#Multiply by 3 
my_value = 9
my_value *=3
# print(my_value)

#Multiply by 10 
mileage = 15 
mileage *=10
# print(mileage)

#Divide by 2 
pizza_slices = 8
pizza_slices /= 2
# print(pizza_slices)

#Divide by 7 
fees = 8.90 
fees /= 7
# print(fees)

#Raise to the 3rd power
num_three = 6
num_three **=3
# print(num_three)

#Raise to the 2nd power **
data = 16 
data **=2
# print(data)

#Integer division, how many times does 3 go into 16?
val_one = 16
val_one //=3
# print(val_one)

## Integer divde by 4 //
val_two = 9 
val_two //= 4
# print(val_two)

# Modulus we use often to find if a value is odd or even
#Find the remainder if divided by 3 
val_three = 10
val_three %=3
# print(val_three)

#find the remainder if divided by 5 %
val_four = 14
val_four %=5
# print(val_four)

#Refactor  me with shortcut operators
fahrenheit = 89
celsius = (fahrenheit - 32) * 5/9
# print(celsius)

fahrenheit -= 32 #parentheses
fahrenheit *= 5/9
celsius = fahrenheit
# print(celsius)

# boolean
print(7>5)

# Is 4 less than or equal to 4
print(4 <= 3)
result = 4 <= 3
print("Is 4 greater than 3?", result)

# Is 6 greater than or equal to 2?
print(6>=2)
result = 6>=2
print("Is 6 greater than or equal to 2?", result)

#Is 5 greater than or equal to 6? >=
print(5>=6)
result = 5>=6
print("Is 5 greater than 6?" , result)

#Is 5 equal to 5? ==
print (5==5)
result = 5==5
print("Is 5 equal to 5?", result)

#Is 100 not equal to 75? !=
print(100 != 75)
result = 100 != 75
print("Is 100 not equal to 75?", result)

# AND && 
# print (5 ==5 and 4 == 4) # True
# print(2==2 and 3 ==1) #False
# print(1==2 and 2 ==10) #False

log_1 = (5==3)
log_2 = (4==7)
print("Log 1 " , log_1)
print("Log 2", log_2)

## OR 
print(5==5 or 5 ==3) #True if at least 1 is true 

## ASSIGNMENT 
