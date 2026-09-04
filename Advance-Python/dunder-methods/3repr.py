""" 

=> __repr__ 

    __repr__ is a dunder method that defines the developer-oriented string
      representation of an object.

    -> “How should this object describe itself to a programmer?”  

"""

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"User(name={self.name!r}, age={self.age!r})"


user = User("Parveen", 22)

print(user)


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"User(name={self.name!r}, age={self.age!r})" # !r means use repr() for this value.

    def __str__(self):
        return f"{self.name}, {self.age} years old"


user = User("Parveen", 22)

print(repr(user))
print(str(user))