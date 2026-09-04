from component import FileSystemComponent

class File(FileSystemComponent):
    """ Leaf object """

    def __init__(self , name : str , size : int) -> None:
        self.name = name 
        self.size = size

    def display(self , indent:int = 0) -> None:
         print(" " * indent + f"{self.name} ({self.size} KB)")    