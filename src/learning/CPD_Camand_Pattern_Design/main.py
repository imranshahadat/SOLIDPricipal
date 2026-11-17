from .chef import Chef
from .order_commands import BurgerOrder, PizzaOrder
from .waiter import Waiter


def run_restaurant() -> None:
    head_chef = Chef()
    waiter = Waiter()

    order_1 = BurgerOrder(head_chef)
    order_2 = PizzaOrder(head_chef)

    waiter.take_order(order_1)
    waiter.take_order(order_2)

    waiter.send_orders_to_kitchen()
    waiter.cancel_last_order()


if __name__ == "__main__":
    run_restaurant()
