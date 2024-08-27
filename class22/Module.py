from datetime import datetime


"""
Create an Employee class 
 * __str___(): return a string representation 
 * years_worked(): Use the datetime module 
 * total_expense()
 * print_employee_information(): store in a txt file (class 18)
 * accessor / mutator 
 * when writing the constructor specify the type 

 - Create your class in another file and run it from test
 Attributes
 - Use type hinting in constructor 
 
"""

class Employee: 

    ## FIELDS 
    # name: string​
    # job_title: string​
    # department: string​
    # salary: float​
    # hire_year: int or string​ 

    def __init__(self, name:str, job_title:str, department:str, salary:float, hire_year:str):
        self.name = name
        self.job_title = job_title
        self.department = department
        self.salary = salary
        self.hire_year = hire_year

    ## Implement str method
    def __str__(self):
        return f"{self.name}\n{self.job_title}\n{self.department}\n{self.salary}\n{self.hire_year}"
    
    ## Accessor Mutator Methods
    def get_name(self):
        return self.name
    
    def set_name(self, name:str):
        self.name = name

    ### Years Worked
    def years_worked( date):
        current_year = datetime.now().year
        return current_year - date
    
    ## Total Expense 
    def total_expense(self, salary):
        years = self.years_worked(self.hire_date)
        return years * salary
    
    ###### print employee name, job title, department, salary, 
    # and hire year to a text file named after the employee.

    def print_emp_information(employee):

