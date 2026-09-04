#  Recieve perform the real work 


class Light:
    "Reciever"

    def turn_on(self) -> None:
        print("Light turn on")

    def turn_off(self) -> None:
        print("Light turn off")          # light class knows nthing about commands     