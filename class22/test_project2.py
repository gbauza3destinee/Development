from Module import Employee

emp = Employee("Sally", "Programmer Analyst","Tech","50000","05-03-2020")

### Test 4 methods + accessor/mutator methods

## Print name                                --- Works 
# print(emp.get_name())
# print(emp.get_hire_year())

## Open CSV file with employee information  --- Faulty 
# emp.print_emp_information()

## Calculate from int to int years worked  --- Test
# print(emp.years_worked())

## Calculate total $ amount of years employee has worked 
# print(emp.total_expense())

## Print to String method -- Works 
# print(emp.__str__())