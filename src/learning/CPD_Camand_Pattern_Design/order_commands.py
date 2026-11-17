from .chef import Chef
from .INTERFACE import Command


class BurgerOrder(Command):
    def __init__(self, chef: Chef) -> None:
        self.chef = chef

    def execute(self) -> None:
        self.chef.cook_burger()

    def undo(self) -> None:
        self.chef.cancel_burger()


class PizzaOrder(Command):
    def __init__(self, chef: Chef) -> None:
        self.chef = chef

    def execute(self) -> None:
        self.chef.cook_pizza()

    def undo(self) -> None:
        self.chef.cancel_pizza()
