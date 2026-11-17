from .interface import PaymentStrategy


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Paid ${amount} using Credit Card.")


class CashPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Paid ${amount} in Cash.")


class BankTransferPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Paid ${amount} via Bank Transfer.")
