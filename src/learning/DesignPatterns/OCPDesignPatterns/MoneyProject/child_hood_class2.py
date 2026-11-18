from .main_class import MAinClass
from .money import Money


class ChildHoodclass2(MAinClass):

    def sendmoney(self, money: Money):
        print("ChildHoodclass2 hun")
        print(f"Amount: {money.send}")
        print(f"Description: {money.desc}")
