from abc import ABC,abstractmethod


class Bevarages(ABC):
    @abstractmethod
    def getCoffeePrice(self) -> int:
        pass
    @abstractmethod
    def getCoffeeDescribtion(self) -> str:
        pass

