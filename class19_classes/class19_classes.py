## classes in python 

## instantiate a class 
"""
class <ClassName> (object):
    Constructor- 
    def_init(self)

    Instance of Class- 
    this --> self 

    When you refer to attributes within this class you must say 
    self.attribute_name 

"""

## example class 

class Point2d():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    ## str method let's you choose what happens 
    ## when you print an instance of the class
    def __str__(self):
        return f"(Your first parameter is {self.x}, your second parameter is {self.y})"
    ## check for equality for two objects
    def __eq__(self,other):
        if self.x == other.x and self.y == other.y: 
            return True
        return False
    def __sub__ (self, other):
        return Point2d(self.x - other.x, self.y - other.y)
    def __add__ (self, other):
        return Point2d(self.x + other.x, self.y + other.y)
    def __lt__ (self, other):
        if self.x < other.x and self.y < other.y:
            return True
        return False
    

## creating an object 
point1 = Point2d(2,3)
point2 = Point2d(2,3)

## __eq 

## sub 

class Date:
    def __init__(self, year=1970,month=1, day=1):
        self.year = year
        self.month = month  
        self.day = day
    
    def __str__(self):
        return f"{self.month:02d}/{self.day:02d}/{self.year}"
    
    def __eq__ (self, other):
        if self.year == other.year and self.month == other.month and self.day == other.day:
            return True
        return False
    def __lt__(self, other):
    #    selfdate = datetime(self.year, self.month, self.day)
    #    otherdate = datetime(other.year, other.month, other.day)
        pass
my_date = Date(2004,10,4)
my_date2 = Date(2003,5,3)
# print(my_date.year)  # prints 1970
# print(my_date)

## Checking equality in two ways
# print("Equals symbol" , my_date == my_date2)
result = Date.__eq__(my_date2, my_date)
# print("Eq method " , result)


## Checking for lesser / greater than 
result = Date.__lt__(my_date, my_date2)
# print(result)


#### leap Year 
from datetime import datetime 

def is_leap_year(date):
    if date.day == 29 and date.year %4 ==0: 
        return True
    return False

my_date = Date(2005,2,29)
print(is_leap_year(my_date))