from component import SimpleCoffee
from decorators import (
    MilkDecorator,
    SugarDecorator,
    WhippedCreamDecorator,
)


def main() -> None:
    coffee = SimpleCoffee()

    print("Base Coffee")
    print(coffee.description())
    print(coffee.cost())

    print("-" * 40)

    coffee = MilkDecorator(coffee)
    coffee = SugarDecorator(coffee)
    coffee = WhippedCreamDecorator(coffee)

    print("Customized Coffee")
    print(coffee.description())
    print(coffee.cost())


if __name__ == "__main__":
    main()