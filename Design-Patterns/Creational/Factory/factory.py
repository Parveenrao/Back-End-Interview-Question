# Concrete Implementations 

from typing import Type

from notification import Notification

class NotificationFactory:


    _registry : dict[str , Type[Notification]] = {}

    @classmethod
    def register(cls , notification_type : str , notification_class : Type[Notification]) -> None:

        cls._registry[notification_type.lower()] = notification_class

    @classmethod
    def create(cls , notification_type : str) -> Notification:

        notification_class = cls._registry.get(notification_type.lower())

        if notification_class is None:
            raise ValueError(
                f"Unknown notification : {notification_type}"
            )   

        return notification_class() 

