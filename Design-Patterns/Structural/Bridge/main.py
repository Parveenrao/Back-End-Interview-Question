from concrete import EmailNotification , SMSNotification , SlackSender

from Refined_abs import UrgentNotification , NormalNotificaiton

def main()-> None:

    email = EmailNotification()
    sms = SMSNotification()
    slack = SlackSender()

    normal_email = NormalNotificaiton(email)

    urgent_sms = UrgentNotification(sms)

    urgent_slack = UrgentNotification(slack)

    normal_email.notify("Daily Report Generated")

    urgent_slack.notify("Server CPU usuage is 90%")

    urgent_sms.notify("Database connection lost")


if __name__ == "__main__":
    main()

