""" 

=> Association 

   -> One object use , knows about or interact with another object, but both exist 
      independently

    -> Teacher ---- teaches ----- student

    A teacher interact with student , but teacher does not own or create students  



"""


class Student:
    def __init__(self , name):
        self.name = name  


class Teacher:
    def __init__(self , name):
        self.name = name 

    def teach(self , student):
        print(f"{self.name} teaches {student.name}") 

student = Student("Parveen")

teacher = Teacher("John")

teacher.teach(student)


# One to One association  , one object is assoicated with one other object


class Passport:
    def __init__(self , number):
        self.number = number


class Person:
    def __init__(self , name , passport):
        self.name = name 
        self.passport = passport


passport = Passport("3432423")

person = Person("Parveen" , passport)

print(person.passport.number)                

# One to many , One teacher many students 

class Student:
    def __init__(self , name):
        self.name = name


class Sir:
    def __init__(self, name):
        self.name = name 
        self.students = []

    def add_students(self, student):
        self.students.append(student)


s = Student("parveen")
s2 = Student("John")

sir = Sir("Lonely")

sir.add_students(s)

sir.add_students(s2)


# Many to one , Many emp into one dep 


class Department:
    def __init__(self , name):
        self.name = name 


class Employee:
    def __init__(self , name , department):
        self.name = name 
        self.department = department



engineeering = Department("Eng")

e1 = Employee("Parveen" , engineeering)

e2 = Employee("John" , engineeering)

e3 = Employee("Lonely" , engineeering)

print(e1.name)
print(e1.department.name)


# Many to Many , many courses and mnay students 


class Course:
    def __init__(self , name):
        self.name = name 


class Students:
    def __init__(self , name):
        self.name = name 
        self.courses = []    

    def enroll(self, course):
        self.courses.append(course)


c1 = Course("java")

c2 = Course("python")

s1 = Students("Parveen")

s2 = Students("john")

s1.enroll(c1)

s1.enroll(c2)

print(s1.courses.name)