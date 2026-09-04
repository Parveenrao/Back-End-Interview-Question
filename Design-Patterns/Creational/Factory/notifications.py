# Concrete Classes

from notification import Notification
from factory import NotificationFactory

# Email Notifications 
class EmailNotification(Notification):

    def send(self):
        print("Email sent")

# SMS Notification 
class SMSNotification(Notification):

    def send(self):
        print("SMS sent") 

# Push Notification 
class PushNotification(Notification):

    def send(self):
        print("Push Send")


# Whatsapp Notification 
class WhatsappNotification(Notification):

    def send(self):
        print("Whatsapp Sent")

# Register classess

NotificationFactory.register(
    "email" , EmailNotification
)

NotificationFactory.register(
    "sms" , SMSNotification
)

NotificationFactory.register(
    "push" , PushNotification)

NotificationFactory.register(
    "whatsapp" , WhatsappNotification
)




