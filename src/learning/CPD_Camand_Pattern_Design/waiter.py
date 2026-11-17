from .INTERFACE import Command


class Waiter:
    def __init__(self) -> None:
        self.order_queue: list[Command] = []
        self.order_history: list[Command] = []

    def take_order(self, command: Command) -> None:
        print("Waiter: Order slip added to notepad.")
        self.order_queue.append(command)

    def send_orders_to_kitchen(self) -> None:
        print("\nWaiter: Sending all orders to the kitchen...")
        while self.order_queue:
            current_order = self.order_queue.pop(0)
            current_order.execute()
            self.order_history.append(current_order)

    def cancel_last_order(self) -> None:
        if self.order_history:
            print("\nWaiter: Customer changed their mind! Canceling last order...")
            last_order = self.order_history.pop()
            last_order.undo()
        else:
            print("\nWaiter: No orders to cancel.")



# from .chef import Chef
# from .order_commands import BurgerOrder, PizzaOrder
# from .waiter import Waiter


# def run_restaurant() -> None:
#     chef = Chef()
#     waiter = Waiter()

#     # 1. Order a Burger
#     burger = BurgerOrder(chef)
#     waiter.take_order(burger)
#     waiter.send_to_kitchen()

#     print("---")

#     # 2. Order a Pizza, then cancel it
#     pizza = PizzaOrder(chef)
#     waiter.take_order(pizza)
#     waiter.send_to_kitchen()
#     waiter.cancel_order()


# if __name__ == "__main__":
#     run_restaurant()
