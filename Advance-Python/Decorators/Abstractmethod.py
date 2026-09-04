"""

=> Abstract Method

   -> An abstract method is a method that declares what should be done but not how 
      it should be done

   -> it force every child class to provide its own implementation

   -> Think of contract 

       if you inherit from me , you must implement this method   



 """

from abc import ABC, abstractmethod


class Notification(ABC):

    @abstractmethod
    def send(self, message: str) -> None:
        pass


class EmailNotification(Notification):

    def send(self, message: str) -> None:
        print(f"Email: {message}")

class SMSNotification(Notification):

    def send(self, message: str) -> None:
        print(f"SMS: {message}")        
