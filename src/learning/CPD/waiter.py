from .Interface import InterFace_Command


class Waiter:
    def __init__(self) -> None:
        self.order: InterFace_Command | None = None  # Holds one order slip

    def take_order(self, order: InterFace_Command) -> None:
        self.order = order  # Save the order slip

    def send_to_kitchen(self) -> None:
        if self.order:
            self.order.execute()  # Run execute()

    def cancel_order(self) -> None:
        if self.order:
            self.order.undo()  # Run undo()
                    # Tell chef to cancel it
