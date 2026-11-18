from dataclasses import dataclass
from abc import ABC,abstractmethod
@dataclass
class BasePet:
    name:str

class BasePetInterface(ABC):

    @abstractmethod
    def petname(self, basepet: BasePet):
        pass


class BaseFlyClass(ABC):

    @abstractmethod
    def fly(self, basepet: BasePet):
        pass


class BaseRunClass(ABC):

    @abstractmethod
    def run(self, basepet: BasePet):
        pass


class BaseEatClass(ABC):

    @abstractmethod
    def eat(self, basepet: BasePet):
        pass



class CatClass(BasePetInterface, BaseEatClass, BaseRunClass):

    def petname(self, basepet: BasePet):
        print(f"My name is {basepet.name}")

    def eat(self, basepet: BasePet):
        print(f"{basepet.name} can eat")

    def run(self, basepet: BasePet):
        print(f"{basepet.name} can run")   

# Bird can eat and fly
class BirdClass(BasePetInterface, BaseEatClass, BaseFlyClass):

    def petname(self, basepet: BasePet):
        print(f"My name is {basepet.name}")

    def eat(self, basepet: BasePet):
        print(f"{basepet.name} can eat")

    def fly(self, basepet: BasePet):
        print(f"{basepet.name} can fly")

class FishClass(BasePetInterface, BaseEatClass):

    def petname(self, basepet: BasePet):
        print(f"My name is {basepet.name}")

    def eat(self, basepet: BasePet):
        print(f"{basepet.name} can eat")
