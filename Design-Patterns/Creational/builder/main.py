from builder import HouseBuilder


def main()-> None:

    luxry_house = (
        HouseBuilder().foundation("Concrete")
        .walls("Brick")
        .roofs("Tiles")
        .doors(2)
        .windows(8)
        .garage()
        .swimming_pool()
        .build()

    )

    luxry_house.display()


if __name__ == "__main__":
    main()    