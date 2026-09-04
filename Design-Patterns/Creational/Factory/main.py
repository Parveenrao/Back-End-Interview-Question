from factory import NotificationFactory
import notifications





def main():

    while True:

        print("\nAvailable notifications")
        print("email")
        print("push")
        print("sms")
        print("whatsapp")
        print("exit")

        choice = input("\nEnter notification type :").lower()

        if choice == "exit":
            break

        try:

            notification =  NotificationFactory.create(choice)

            notification.send()

        except ValueError as e:
            print(e)    



if __name__ == "__main__":
    main()