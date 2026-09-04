from state import State
from playing_state import PlayingState


class StoppedState(State):

    def play(self, player: "MediaPlayer") -> None:
        print("Starting Playback")
        player.state = PlayingState()

    def pause(self, player: "MediaPlayer") -> None:
        print("Cannot pause. Player is stopped.")

    def stop(self, player: "MediaPlayer") -> None:
        print("Already stopped.")