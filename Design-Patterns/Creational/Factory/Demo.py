""" 

=> Factory Design Pattern 

    -> Factory design pattern is a type of creational design pattern.

    -> It helps creates object without exposing the object creation logic to the client



"""


from abc import ABC , abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self):
        pass 


# Concrete products 

class EmailNotification(Notification):

    def send(self):
        print("Sending email") 


class SmsNotification(Notification):

    def send(self):
        print("Sending SMS notification")

class PushNotification(Notification):

    def send(self):
        print("Sending Push notifications")



# Factory class 


class NotificationFactory:

    @staticmethod
    def create_notification(notification_type):

        if notification_type == "email":
            return EmailNotification()
        
        elif notification_type == "sms":
            return SmsNotification()

        elif notification_type == "push":
            return PushNotification()

        else:
            raise ValueError("Invalid Notification type")


notification = NotificationFactory.create_notification("sms")

notification.send()
