# These classes not care about whether class are sms and email 


from abstraction import Notification

class NormalNotificaiton(Notification):

    def notify(self ,message : str) -> None:
        self._sender.send(message)


class UrgentNotification(Notification):

    def notify(self , message : str) -> None:

        self._sender.send(f" Urgent {message}")        