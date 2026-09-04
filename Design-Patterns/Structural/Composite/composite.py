from component import FileSystemComponent


class Folder(FileSystemComponent):

    def __init__(self , name : str) -> None:
        self.name = name 
        self.children : list[FileSystemComponent] = []

    def add(self, component : FileSystemComponent) -> None:
        self.children.append(component)

    def remove(self , component : FileSystemComponent) -> None:
        self.children.remove(component)

    def display(self, indent : int = 0) -> None:
        print(" " * indent + f"📁 {self.name}")

        for child in self.children:
            child.display(indent + 4)
