from datetime import datetime
import pandas as pd
import os




"""
Create an Employee class 
 * __str___(): return a string representation 
 * years_worked(): Use the datetime module 
 * total_expense()
 * print_employee_information(): store in a txt file (class 18)
 * accessor / mutator 
 * when writing the constructor specify the type 

 - Create your class in another file and run it from main
 - Use type hinting in constructor 
 
"""
class Employee: 

    ### * Fix Type Cast of hire_year: 
    #  I've typehinted hire year to be int but it's coming out as a string
    #   current_year(int) - self.hire_year (int)
    ### * Test total_expense method 
    ### * Fix name of file printed out in printempinfo

    ### Verify that csv file is printing in the correct format expected.

    ## FIELDS 
    # name: string​
    # job_title: string​
    # department: string​
    # salary: float​
    # hire_year: int or string​ 

    def __init__(self, name:str, job_title:str, department:str, salary:float, hire_year:int):
        self.name = name
        self.job_title = job_title
        self.department = department
        self.salary = salary
        self.hire_year = hire_year

    ## Implement str method
    def __str__(self):
        return f"{self.name}\n{self.job_title}\n{self.department}\n{self.salary}\n{self.hire_year}"
    
    ## Accessor & Mutator Methods
    def get_name(self):
        return self.name
    
    def set_name(self, name:str):
        self.name = name

    def get_job_title(self):
        return self.job_title
    
    def set_job_title(self, job_title: str):
        self.job_title = job_title
    
    def get_department(self):
        return self.department
    
    def set_department(self, department: str):
        self.department = department
    
    def get_salary(self):
        return self.salary
    
    def set_salary(self, salary: float):
        self.salary = salary
    
    def get_hire_year(self):
        return self.hire_year
    
    def set_hire_year(self, hire_year: int):
        self.hire_year = hire_year

    ####################################### Business Logic ###########################

    ### Years Worked
    def years_worked(self):
        current_year = datetime.now().year
        print(f"Current year type {type(current_year)}")
        hire_year_converted = int(self.hire_year)
        print(f"hire year type {type(self.hire_year)}")

        # return current_year - self.hire_year
    
    ## Total Expense
    def total_expense(self, salary):
        years = self.years_worked(self.hire_year)
        return years * salary
    
    ###### Print employee information to a text file
    def print_emp_information(self):
        # os.chdir(os.path.dirname(os.path.abspath(__file__)))
        employee_dict = self.__dict__
        print(employee_dict)
        df = pd.DataFrame.from_dict([employee_dict])
        name = employee_dict["name"]
        print(name)
        df.to_csv('f{name}.csv', index=False)


