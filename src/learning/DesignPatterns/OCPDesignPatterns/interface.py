
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Money:
    send: int
    desc: str


class MAinClass(ABC):

    @abstractmethod
    def sendmoney(self, money: Money):
        pass


class ChildHoodclass(MAinClass):

    def sendmoney(self, money: Money):
        print("ChildHoodclass hun")
        print(f"Amount: {money.send}")
        print(f"Description: {money.desc}")


class ChildHoodclass2(MAinClass):

    def sendmoney(self, money: Money):
        print("ChildHoodclass2 hun")
        print(f"Amount: {money.send}")
        print(f"Description: {money.desc}")


class TUmsbmerybinaKuchnahimerabacha:

    def Mainhisbkuchhun(self, trandfer: MAinClass, money: Money):
        trandfer.sendmoney(money)


a1 = ChildHoodclass()
b2 = ChildHoodclass2()
c3 = TUmsbmerybinaKuchnahimerabacha()

money = Money(899883, "First transfer")

c3.Mainhisbkuchhun(a1, money)
c3.Mainhisbkuchhun(b2, money)
