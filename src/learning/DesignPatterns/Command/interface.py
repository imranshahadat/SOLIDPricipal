from abc import ABC,abstractmethod
from dataclasses import dataclass


@dataclass
class CookInterface:
    cook:str


class CookabstractInterface(ABC):
    @abstractmethod
    def order(self,msg:CookInterface):
        pass  


class CookPizza:
    def cook_bureget(self):
        print("pizzaiscooking")
    def cook_burger(self):
        print("buer is preparing")    