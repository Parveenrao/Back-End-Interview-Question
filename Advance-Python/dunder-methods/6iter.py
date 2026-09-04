""" 

=> __iter__

   -> Makes an object iterable , meaning we can loop over it with for 


"""


class Students:
    def __init__(self):
        self.name = ["parven" , "john" , "hello"]

    def __iter__(self):
        return iter(self.name)


s = Students()

for name in s:
    print(name)