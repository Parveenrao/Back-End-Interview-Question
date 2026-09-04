

# Strategy pattern  for naviagtaion map using , ggpple 


from abc import ABC , abstractmethod


class RouteStrategy(ABC):

    @staticmethod
    def build_route(start :str , end : str) -> None:
       pass



# concrete strategy , first car 

class CarStrategy(RouteStrategy):

    @abstractmethod
    def build_route(self , start :str , end : str) -> None:
        print(f"Bike route {start} -> {end}")
        print("Optimized for roads and bikes")


# bike staratefgy 

class BikeStrategy(RouteStrategy):

    @staticmethod
    def build_route(start : str , end : str) -> None:
        print(f"Build rout {start} -> {end}")
        print("Opitimzed for bike-friendly roads")

# walk strategy 


class WalkStrategy(RouteStrategy):

    @staticmethod
    def build_route(start : str , end : str) -> None:
        print(f"Build route {start} -> {end}")
        print("Optimized route for walking")


# now navigation making them chageable at runtime 


class Navigation:

    def __init__(self , strategy : RouteStrategy) -> None:
        self.strategy = strategy

    @property
    def strategy(self)  -> RouteStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self , strategy : RouteStrategy) -> None:
        self._strategy = strategy

    def build_route(self , start : str , end : str) -> None:
        return self._strategy.build_route(start , end)



def main() -> None:

    naigvation = Navigation(WalkStrategy)

    naigvation.build_route("Delhi" , "Mumabi")


    naigvation.strategy = WalkStrategy()
    naigvation.build_route("Ghr" , "Zhome")

if __name__ == "__main__":
    main()            