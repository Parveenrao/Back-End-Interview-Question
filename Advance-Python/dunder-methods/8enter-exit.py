""" 

=> Enter Exit Dunder method in python 


    -> __enter__ and __exit___ are the dunder method used by contxt managers.

    -> they are what make the with statement work



"""

class Test:

    def __enter__(self):
        print("Start")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exception type:", exc_type)
        print("Exception:", exc_value)
        print("End")


with Test():
    x = 10 / 0