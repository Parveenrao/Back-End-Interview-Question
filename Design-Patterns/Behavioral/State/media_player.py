from state import State

from stopped_state import StoppedState


class MediaPlayer:

    """ Delegates behaviour to the current state"""

    def __init__(self) -> None:

        self._state : State = StoppedState()

    @property
    def state(self) -> state:
        return self._state

    @state.setter
    def state(self ,state  : State) -> None:
        self._state = self.state

    def play(self) -> None:
        self._state.play(self)

    def stop(self) -> None:
        self._state.stop(self) 

    def pause(self) -> None:
        self._state.pause(self)
        
                       