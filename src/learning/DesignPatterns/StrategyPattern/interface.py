from abc import ABC,abstractmethod

class BaseDiscount(ABC):
    @abstractmethod
    def BaseTotal(self):
        pass

   