from abc import ABC,abstractmethod

class Mainclass(ABC):
    def __int__(self):
        pass
    @abstractmethod
    def Factory(self)->str:
        pass