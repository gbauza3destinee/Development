### 

''' Loops and Conditionals

-- Break stops all iterations
-- Continue meets the condition and continues to the next iterations

-- Pass continues despite any errors

What is the difference between a For and While Loop?

For Loops help us loop through interables (strings, lists, tuples). While loops allow us to effectively target conditions.


How do I write a For Loop?


animal = 'dog'

for a in animal:
    print(a)

Result:
d
o
g

How do I write a While Loop?

start = 0
end = 10

while start <= end:
    print(start)
    start += 1

'''


''' Break Keyword

Break is a keyword that when placed in a loop will leave the loop without executing any more code when the keyword is reached.

In example 1, we have to re-enter the loop after the stop condition is entered by the user

In example 2, we are able to break out of the loop as soon as we fulfill our condition

'''
# Example 1
# userin = ''

# while userin != 'stop':
#     userin = input("Please enter your text or type \'stop\' to stop: ").casefold()
#     print('We are going back to try to re-enter the loop, and test your input')

# Example 2
# userin = ''

# while True:
#     userin = input("Please enter your text or type \'stop\' to stop: ").casefold()
#     if userin == 'stop':
#         print('Goodbye, I am stopping now')
#         break



'''
------> Review 
Write some code that takes in numbers from a user one at a time. 
This should keep going until the user enters 0. Then print the 
sum of all the numbers. If the user inputs something that isn't a
 number, an error message should appear and the program should stop. 
 (Hint: use break)

Example (no error):
5
12
0
Sum: 17

Example (error):

5
7
c
Error: Not a number
'''
# total = 0
# userData = input("Enter a number")

# while True: 
#     if not userData.isnumeric():
#         print("Error not a number")
#         break
#     elif userData == 0: 
#         print("Sum is " + total)
#         break
#     else: 
#         total += int(userData)






'''5 Letter Word Program
Create a program which accepts only words with 5 letters.
 If the user inputs any other word with more than or 
 less than 5 letters, force them to start over again.
   If the word has 5 letters, congratulate the user on 
   inputting a 5 letter word
'''
## -- Runs
# userIn = input("Write a 5 letter word")

# for n in userIn : 
#     if len(userIn) == 5:
#         print("Congratulations -- Word accepted")
#         break
#     else: 
#         print("Try again!")
#         continue

'''
Example

Use the continue keyword to loop through a string and only print the vowels.

'''
# word = "hello"

# for n in word : 
#     if n in "aeiou":
#         print(n)
#         continue

'''
----> review 
Exercise: Sum of even digits

Take a string as user input, and verify that it's a number.
Loop through each digit of the number, and only add it to the sum if it's even.
Print the sum of all the even digits at the end. 
Make sure to use the continue keyword.
'''



while True: 
    sum = 0
    str1 = input("Enter a number: ") 

    if str1.isnumeric():
        for n in str1:
            n = int(n)
            if n %2 ==0:
                sum+=n
        print(sum)
        continue
    else:
        print(f"Please enter a number, {str1} is not a number")





''' Break vs. Continue '''

word = 'hello'
vowels = ['a', 'e', 'i', 'o', 'u']

# for w in word:
#     if w in vowels:
#         print(w)
#         break


# for w in word:
#     if w in vowels:
#         print(w)
#         continue


''' Pass keyword - placeholder'''

season = 'summer'

# for s in season:
#     pass


'''

Write some code that takes in strings from a user one at a time.
After each string is taken in evaluate if the string is empty,
a number, a set of letters, or contains symbols.
If the string is empty, stop the loop.
If the string is a number, convert it to a float and add it to a total.
If the string is a set of letters, 
concatenate to the other letter strings passed in.
If it contains a symbol, or is none of the above, do nothing and repeat the loop.
Make sure to use break and/or continue.
'''

''' Let's Make a Plan'''

''' Following the plan '''
# # initialize variables to capture string and total
# word = input("Enter a word")
# # start loop
# total = 0

   
 
# # get string
# while True:   
# # If the string is empty, stop the loop

#     if word == "":
#             print("char is empty")
#             break
# # If the string is a number, convert it to a float and add it to a total

#     elif word.isnumeric() : 
#        num = float(word)
#        total += num
#        print(f"Your total is{num}")
#        continue
# # If the string is a set of letters, concatenate to the other letter strings passed in.
#     elif word.isalpha:
#         word += word
#         print(f"Your string is {word}")
#         continue

# # If it contains a symbol, or is none of the above, do nothing and repeat the loop

#     elif word.isalnum():
#             continue
''' Following the plan '''



''' While Else and For Else

Discussion:
What is the output of this code?
What would the output be if i is initialized to 6?

'''

# i = 3
# while i > 0:
#     print(i)
#     i -= 1
#     if i == 4:
#         break
# else:
#     print('done')


''' More fun while true!

Write a while true loop that will keep asking the day of the week until you type in Monday

'''

