from .chef import Chef
from .waiter import Waiter
from .workercammad import BurgerOrder


chef = Chef()
waiter = Waiter()

burger = BurgerOrder(chef)

waiter.take_order(burger)
waiter.send_to_kitchen()  # Calls execute()
waiter.cancel_order()     # Calls undo()
