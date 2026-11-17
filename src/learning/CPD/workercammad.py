from .Interface import InterFace_Command
from .chef import Chef
# 3. order_commands.py (Concrete Commands)
class BurgerOrder(InterFace_Command):
    # which chef want to use 
    # which things you want to use 
    # what is the work that you need
    def __init__(self,chef:Chef)-> None:
        # i have chef i have a worker
        self.chef = chef
# which is the specific work you want or expecting from this class
    def execute(self) -> None:
        self.chef.cook_burger()    
    def undo(self) -> None:
        self.chef.cancel_burger()


class PizzaOrder(InterFace_Command):
    def __init__(self, chef: Chef) -> None:
        self.chef = chef

    def execute(self) -> None:
        self.chef.cook_pizza()

    def undo(self) -> None:
        self.chef.cancel_pizza()        


