""" 

=> DataClass Decorator 

    -> dataclass automatically generates common method for a class such as

       1. __init__()
       2. __repr__()
       3. __eq__()
       4. __hash__()

       5. ordering methods __lt__ , __gt__



"""

# without dataclasss

class Employee:

    def __init__(self, name : str , age : int , salary : float) -> None:
        self.name = name 
        self.age = age 
        self.salary = salary

    def __repr__(self):

        return (
            f"Employee(name = '{self.name}') ,"
            f"age = {self.age} ,"
            f"salary = {self.salary}"
        )
    
    def __eq__(self, other):

        if not isinstance(other , Employee):
            return False

        return (

            self.name == other.name and 
            self.age == other.age and 
            self.salary == other.salary
        ) 
        
        

emp1 = Employee("Parveen", 22, 50000)
emp2 = Employee("Parveen", 22, 50000)          # we have to write so much

print(emp1)
print(emp1 == emp2)        


# now with dataclass

from dataclasses import dataclass

@dataclass
class Parveen:
    name : str 
    age : int 
    salary : float


emp1 = Employee("Parveen", 22, 50000)
emp2 = Employee("Parveen", 22, 50000)

print(emp1)
print(emp1 == emp2)


# default values in dataclass

@dataclass
class John:

    name : str 
    age : int 

    salary : float = 50000

emp = John("Parveen", 22)

print(emp)    


# adding your own methods 

@dataclass 
class Hello:

    name : str 
    salary : float

    def yearly_salary(self) -> float:
        return self.salary * 12
    

# common dataclass parameters

@dataclass(
    init=True,
    repr=True,
    eq=True,
    eq=True,
    order=False,
    frozen=False
)


# is dataclass immutable by default , no by default dataclass instance are mutable . to make mutable 

@dataclass(frozen=True)
class Employee:
    ... 