from state import State



class PlayingState(State):
    """ Representing the playing state"""

    def play(self , player : "MediaPlayer") -> None:
        print("Already playing")

    def pause(self , player : "MediaPlayer") -> None:
        print("Pausing music .....")

        player.state = PausedState()

    def stop(self,  player : "MediaPlayer") -> None:
        print("Stopping music")

        player.state = StoppedState()
