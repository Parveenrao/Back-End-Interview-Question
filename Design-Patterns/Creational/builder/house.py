# House 


from dataclasses import dataclass

@dataclass
class House:

    foundation : str | None = None
    walls : str | None = None
    roofs : str | None = None
    doors :  int = 0
    windows : int = 0
    garage : bool = False
    swimming_pool = False

    def display(self) -> None:
        print("\nHouse Configuration")
        print("-" * 30)
        print(f"foundations    : {self.foundation}")
        print(f"walls          : {self.walls}")
        print(f"roofs          : {self.roofs}")
        print(f"doors          : {self.doors}")
        print(f"windows        : {self.windows}")
        print(f"garage         : {self.garage}")
        print(f"swimming_pool  : {self.swimming_pool}")


        