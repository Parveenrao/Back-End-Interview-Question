""" 

=> @Property 

    -> The property decorator turns a method into a read-only attribute 



"""

# without property 

class Employee:

    def __init__(self , salary : float) -> None:
        self.salary = salary

    def salary(self) -> float:
        return self.salary


emp = Employee(5000)

print(emp.salary())   # we need paranthesis because salary is a method


# with property

class Employee:
    def __init__(self , salary : float) -> int:
        self._salary = salary

    @property
    def salary(self) -> float:
        return self._salary
    

employee = Employee(5000)

print(employee.salary)


# Property decorator have three methods . getter , seter and deleter

class Employee:

    def __init__(self , name : str , salary : float) -> None:
       self.name = name 
       self.salary = salary

    @property
    def salary(self) -> float:
        # getter return the employee salary
        return self._salary

    @salary.setter
    def salary(self , amount:float) -> None:

        if amount < 0:
            raise ValueError("Salary cannot be negative")

        self._salary = amount

    @salary.deleter
    def salary(self) -> None:

        # deleter , remove salary information

        print("Salary record deleted")

        del self._salary


employee = Employee("Parveen", 50000)

employee.salary

employee.salary = 70000

print(employee.salary)
