# Concrete Subject 


from subject import Subject
from observer import Observer
from typing import List


class WeatherStation(Subject):

    def __init__(self) -> None:

        self._temperature : float = 0
        self._observer : List[Observer] = []

    @property
    def temperature(self , temperature) -> float:
        return self._temperature

    def attach(self , observer : Observer) -> None:
        self._observer.append(observer)
        print(f"{observer.__class__.__name__} subscribed") 

    def detach(self , observer : Observer) -> None:
        self._observer.remove(observer)
        print(f"{observer.__class__.__name__} unsubscribed") 


    def notify(self) -> None:
        print("\nNotifying observer\n") 

        for observer in self._observer:
            observer.update(self._temperature)

    def set_temperature(self , temperature : float) -> None:
        print(f"\nWeather changes to {temperature}C")

        self._temperature = temperature
        self.notify()               
