# Client code 

from reciever import Light

from concrete import TurnOnLight , TurnOfLight

from invoker import RemoteControl


def main() -> None:

    light = Light()

    turn_on = TurnOnLight(light)

    turn_of = TurnOfLight(light)

    remote = RemoteControl()

    remote.set_command(turn_on)

    remote.press_button()

    remote.set_command(turn_of)
    
    remote.press_button()



if __name__ == "__main__":
    main()