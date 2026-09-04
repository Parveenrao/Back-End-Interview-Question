from house import House

class HouseBuilder:
    
    def __init__(self) -> None:
        self._house = House()

    def foundation(self , foundation : str) -> "HouseBuilder":
        self._house.foundation =  foundation

        return self 
    
    def walls(self , walls : str) -> "HouseBuilder":
        self._house.walls = walls
        return self

    def roofs(self , roofs : str) -> "HouseBuilder":
        self._house.roofs =  roofs
        return self   
    
    def doors(self , doors : int) -> "HouseBuilder":
        self._house.doors =  doors
        return self   
    
    
    def windows(self, windows) -> "HouseBuilder":
        self._house.windows = windows
        return self
    

    def garage(self ) -> "HouseBuilder":
        self._house.garage = True
        return self 
    
    def swimming_pool(self ) -> "HouseBuilder":
        self._house.swimming_pool = True
        return self 


    def build(self) -> House:

        if self._house.foundation is None:
            raise ValueError("Foundation is required") 
        
        if self._house.walls is None:
            raise ValueError("Walls are required")
        
        if self._house.roofs is None:
            raise ValueError("Roof is required")
        
        house = self._house

        # reset builder for next builder 

        self._house = House()

        return house