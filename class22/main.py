from Module import Employee

emp = Employee("Sally", "Programmer Analyst","Tech","50000","05-03-2020")

"""                                     Testing all methods    """

## Print Accessor / Mutator methods                           --- Works 
# print(emp.get_name())
# print(emp.get_hire_year())
# print(emp.get_department())
# print(emp.get_salary())
# print(emp.get_job_title())




## Open CSV file with employee information  --- Working, check structure 
emp.print_emp_information()


## Calculate from int to int years worked  --- Faulty type error int to int
# print(emp.years_worked())

## Calculate total $ amount of years employee has worked  --- Test post Years worked
# print(emp.total_expense())

## Print to String method                                    --- Works 
# print(emp.__str__())