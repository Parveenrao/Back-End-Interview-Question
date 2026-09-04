# State interface for all player 

from abc import ABC ,abstractmethod

class State(ABC):
    """ Base Interface for all player states"""

    @abstractmethod
    def play(self , player : "MediaPlayer") -> None:
        ... 

    @abstractmethod
    def pause(self, player : "MediaPlayer") -> None:
        ...

    @abstractmethod
    def stop(self , player : "MediaPlayer") -> None:
        ...         