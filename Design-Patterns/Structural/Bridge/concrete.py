from Implementor import NotificationSender



# Concrete Implementations
# Email sender 

class EmailNotification(NotificationSender):

    def send(self , message : str) -> None:
        print(f"[Email] {message}")


class SMSNotification(NotificationSender):

    def send(self , message : str) -> None:
        print(f"[SMS] {message}")


class SlackSender(NotificationSender):

    def send(self , message : str) -> None:
        print(f"[Slack] {message}")                


# These classes does not know about urgent and normal , their job is to only send        