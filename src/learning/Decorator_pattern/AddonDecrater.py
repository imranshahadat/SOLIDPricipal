from .Interfacee import Bevarages
class AddonDecrater(Bevarages):
    def __init__(self, beverage: Bevarages): 
        self.beverage = beverage
    
    def getCoffeePrice(self) -> int:
        return self.beverage.getCoffeePrice()
        
    def getCoffeeDescribtion(self) -> str:
        return self.beverage.getCoffeeDescribtion()    