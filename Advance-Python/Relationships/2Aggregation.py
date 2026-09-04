""" 

=> Aggregation 

    -> Aggregation HAS-A relationship , but two object can exist independently 


    -> A dept has a employee , but employee exist even if the dept is deleted




"""


class Employee:
    def __init__(self , name):
        self.name = name 


class Department:
    def __init__(self , name):
        self.name = name 
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)  


emp = Employee("Parveen") 

emp2 = Employee("John")

dept = Department("HR")

dept.add_employee(emp)

dept.add_employee(emp2)

print(dept.employees[0].name)


del dept

print(emp.name)
