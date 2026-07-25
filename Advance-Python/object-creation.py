""" 


=> __new__ Vs. __init___ in python 


    -> Both Involved in object creation , but they do different jobs.


    -> ___new___ creates the object , __init___ prepare the object 


    -> Start with normal classs 

          class Student:
             def __init__(self, name):
             self.name = name


          s1 = Student(Parveen)


          python perform two operation

          Student("Parveen")
              |
           __new__() creates student object
              |
          __init__()
              |
              |         sets name = Parveen
              s1 

       -> __new___ = responsible for creating and returing the new object 


"""


class Student:

    def __new__(cls , name):                # why cls , because there is no instance yet. thats exactly python __new__ trying to create
        print("Creating object")
        obj = super().__init__(cls)
        return obj

    def __init__(self , name):
        print("Initialization object") 
        self.name = name