# Concrete Observers 


from observer import Observer

class MobileDisplay(Observer):

    def update(self , temperature:float) -> None:

        print(f"Mobile Display : {temperature} C")


class TVDisplay(Observer):

    def update(self , temperature:float) -> None:

        print(f"TV Display {temperature}C")

class LEDDisplay(Observer):

    def update(self , temperature:float) -> None:
        print(f"Led Display {temperature}C")