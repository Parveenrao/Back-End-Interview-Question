""" 

=> Classmethod 

   -> A class method is method that receives the class itself as the first arguments instead of 
      the instance

   -> It self cls instead of self   



"""


class Employee:

    company = "Google"

    @classmethod
    def show_company(cls) -> None:
        print(cls.company)


# Modifying class Variable 

class Bank:

    interest_rate = 7.5

    @classmethod
    def update_rate(cls , rate : float):
        cls.interest_rate = rate        