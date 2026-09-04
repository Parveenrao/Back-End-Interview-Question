from state import State

from playing_state import PlayingState


class PausedState(State):

    def play(self , player : "MediaPlayer") -> None:
        print("Playing music")

        player.state = PlayingState()

    def pause(self, player : "MediaPlayer") -> None:
        print("Already Paused") 


    def stop(self , player : "MediaPlayer") -> None:
        print("Stopping here")

        player.state = StoppedState()       