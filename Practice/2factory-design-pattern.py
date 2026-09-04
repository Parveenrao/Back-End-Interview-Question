""" 

=> Build a notification system that supports three notification types:

    Email
    Push 
    SMS

    Each notification shoudl have , send(message) method


"""

class EmailNotification:
    def send(self) -> None:
        print("Send Message by Email")

class PushNotification:
    def send(self) -> None:
        print("Send message by Push Notification")

class SMSNotification:
    def send(self) -> None:
        print("Send Message by SMS")


class Factory:

    @staticmethod
    def create_notification(notification_type) -> None:

        if notification_type == "email":
            return EmailNotification()

        elif notification_type == "push":
            return PushNotification()

        elif notification_type == "Sms":
            return SMSNotification()

        else:
            raise ValueError("Invalid notification type")


notification = Factory.create_notification("push")

notification.send()


    

#==============================================================================

# first we make abstract classes , all classes inherit fromthis 


from abc import abstractmethod , ABC

class Notification(ABC):

    @abstractmethod
    def send() ->  None:
        pass

# now concrete implementations



class EmailNotification(Notification):
    def send(self) -> None:
        print("Send Message by Email")

class PushNotification(Notification):
    def send(self) -> None:
        print("Send message by Push Notification")

class SMSNotification(Notification):
    def send(self) -> None:
        print("Send Message by SMS")





# factory class 

class NotificationFactory:

    _registry : dict[str , type[Notification]] = {}

    @classmethod
    def register(cls , notification_type : str , notification_class : str) -> None:

        cls._registry[notification_type.lower()] = notification_class()

    @classmethod
    def create_notification(cls , notification_type : str) -> Notification:

        notification_class = cls._registry.get(notification_type.lower())

        if notification_class is None:
                    raise ValueError(
                        f"Unknown notification : {notification_type}"
                    )   
        
        return notification_class() 


notification = NotificationFactory()

notification.register()