""" 
=> Staticmethod Decoratror In Python 

     -> A static method is a method that belong to class but does not need access to either
        the instance (self) or the class (cls)


"""


class Demo:

    @staticmethod      # does not required self-keyword
    def hello():
        print("Hello")


# static method cannot access instance variable

class Employee:

    def __init__(self):
        self.salary = 5000

    @staticmethod
    def show():
       print(self.salary)    


# we can access the instance varibale using class name 


class Company:

    company = "google"

    @staticmethod
    def show():
        print(Company.company)
