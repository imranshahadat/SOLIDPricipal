from .checkout import ShoppingCart
from .strategies import BankTransferPayment, CashPayment, CreditCardPayment


def run_shop() -> None:
    # 1. Start shopping and choose Credit Card strategy
    cart = ShoppingCart(CreditCardPayment())
    cart.checkout(100.0)

    # 2. Change your mind and swap to Cash strategy at runtime
    cart.set_strategy(CashPayment())
    cart.checkout(50.0)

    # 3. Swap to Bank Transfer strategy
    cart.set_strategy(BankTransferPayment())
    cart.checkout(250.0)


if __name__ == "__main__":
    run_shop()
