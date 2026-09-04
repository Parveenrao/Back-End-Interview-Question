class NotificationService:

    """ Send customer notification"""

    def send_confirmation(self, email:str) -> None:
        print(

            f"[Notification] Confirmation sent to {email}"
        )