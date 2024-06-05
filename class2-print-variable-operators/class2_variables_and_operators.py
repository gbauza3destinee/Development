## 1. Print Statement in Python 
# Uncomment multiple lines at once command + /

# print("Hello")

## Addition
# print(3 + 3)

#Subtraction 
# print(10-7)

#Multiplication
# print(5*5)

#Division 
# print(20/10)
# print(11/3)

# try: 
#     print(5/0)
# except ZeroDivisionError as e:
#     print("You cannot divide by 0")

# #Exponents 
# print(5**2)
# print(2**3)

# Integer Division
# print(10//3)

#Modulo - if remainder is 0 (even) else(odd)
# print(3 % 10)

# #Variables
# num_one =1 
# print(num_one)
# num_two= 20
# print(num_two)

# print(num_two + num_one)
length = 10
width = 7
perimeter = 2*(length + width) 
print(perimeter)


## Identify the data type
fav_color = "blue"
technical_errors= True
num_4 =4.05
print(type(fav_color))
print(type(num_4))

# Lists and looping
student_grades = [100, 95, 70,85, 40]
new_grade = 35

#similar to a foreach loop for(Datatype student : student_grades)
for student in student_grades: 
    print("One grade is: ", student)

student_grades.append(new_grade)
student_grades.remove(new_grade)