
# Component 

from abc import ABC , abstractmethod

class FileSystemComponent(ABC):
    """Base interface for all files and folders"""

    @abstractmethod
    def display(self , indent : int = 0) -> None:

        """Display the component"""