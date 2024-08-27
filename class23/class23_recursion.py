''' Recursion and more brain teasers


FUNCTION
    BASE CONDTION
    RECURSIVE CALL

 '''


''' Lets break Python'''



''' Blast off Recursion Function  

Lets write a recursive function that will count down from nth positve number, down to zero and give a nice message to the user!

'''


''' Blast off recursion in a loop '''




''' Write a function that will 
take in a string and will return a list along 
with the count of each character

Example:

'Saturday'

[S,1,a,2,t,3,u,4,r,5,d,6,a,7,y,8]

'''







''' Using Recursion, lets write a function that will 
count down from an even number down to 0
0 is our base case (when our recursion will stop)

Bonus: Lets put a fix in place to let the user 
know they have to enter an even number
'''
# def even_nums(n):
#     if n %2 != 0:
#         print("You have to enter an even number")
#     elif n > 0 :
#         print(n)
#         even_nums(n-2)
#     else:
#         print("Blast off!")

# even_nums(13)


''' Write a python function that will take in the following dictionary

acct = {"Name": "Joe Smith", "Session Count": 3, "Cost Per Session": 5.50}

and will output a string

'Hello Joe Smith, your balance is 16.50'

'''
acct = {"Name": "Joe Smith", "Session Count": 3, "Cost Per Session": 5.50}


# def print_balance(data):
#     print(f"hello {data["Name"]}, your balance is {data["Session Count"] * data["Cost Per Session"]:02f}")

# print_balance(acct)




''' Factorial
Write a recursive function that will calculate the factorial of a number. The function should take in a number.

How does Factorial work?
n! = n x (n - 1) x (n - 2) x (n - 3) x ... x 1

Factorial of 10
10! = 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1

 '''

# def factorial(num):
#     if num == 1:
#         return num * 1
#     else: 
#         return num * factorial(num - 1)

# print(factorial(5))

''' Sum of natural numbers
Write a function that calculates the sum of the first n 
natural numbers down to 1. Use recursion to solve this problem

10 = 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1

'''
### 10 
def natural_numbers(num):
    if num == 1:
        return num * 1
    else: 
        return num + natural_numbers(num - 1) # 10 + 9 + 8 
    
print(natural_numbers(10))



'''

Exercise
Write a recursive function that multiplies two numbers, using addition.
The function multiply(m, n) should return m*n
'''
def multiply_two_nums(m,n):
    if n == 0 :
        return 0
    else: 
        return m + multiply_two_nums(m, n-1)



'''
Using the previous example as reference, write a recursive function that 
takes one number to the power of another number, using multiplication.
The function power(m, n) should return m**n
'''

def power(m,n):
    if n == 0 :
        return 0
    else: 
        return m * power(m,n-1)




''' More brainteasers, courtesy of https://www.w3resource.com/'''



''' Write a function that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java
'''





'''
September Challenge 

The Fibonacci sequence is a pattern that often appears in nature. This is the pattern: 1, 1, 2, 3, 5, 8, 13, ...
Each number is the sum of the two numbers before it. So, element n of the Fibonacci sequence can be computed like this: n = (n-1) + (n-2)
Patterns like this lend themselves to recursion very naturally.
How would you write a recursive function that computes the first n digits of the Fibonacci sequence?

'''