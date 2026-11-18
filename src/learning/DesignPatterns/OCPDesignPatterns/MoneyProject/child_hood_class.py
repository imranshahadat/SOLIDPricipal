from .main_class import MAinClass
from .money import Money


class ChildHoodclass(MAinClass):

    def sendmoney(self, money: Money):
        print("ChildHoodclass hun")
        print(f"Amount: {money.send}")
        print(f"Description: {money.desc}")
