from .interface import PaymentStrategy


class ShoppingCart:
    def __init__(self, payment_strategy: PaymentStrategy) -> None:
        # Store the chosen strategy
        self.payment_strategy = payment_strategy

    def set_strategy(self, payment_strategy: PaymentStrategy) -> None:
        # Allow swapping the strategy anytime
        self.payment_strategy = payment_strategy

    def checkout(self, amount: float) -> None:
        # Delegate the payment work to the active strategy
        self.payment_strategy.pay(amount)
