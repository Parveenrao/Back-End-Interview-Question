# Client code 

from display import TVDisplay , MobileDisplay , LEDDisplay
from weather import WeatherStation

def main()-> None:

    weather = WeatherStation()

    mobile = MobileDisplay()
    tv     = TVDisplay()
    led    = LEDDisplay()

    weather.attach(tv)
    weather.attach(mobile)
    weather.attach(led)


    weather.set_temperature(25)
    weather.set_temperature(30)


if __name__ == "__main__":
    main()