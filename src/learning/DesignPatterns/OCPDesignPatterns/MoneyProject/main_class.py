from abc import ABC, abstractmethod
from .money import Money


class MAinClass(ABC):

    @abstractmethod
    def sendmoney(self, money: Money):
        pass
