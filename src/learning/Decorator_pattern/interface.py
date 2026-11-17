from abc import ABC,abstractmethod


class Bevarages(ABC):
    @abstractmethod
    def getCoffeePrice(self) -> int:
        pass
    @abstractmethod
    def getCoffeeDescribtion(self) -> str:
        pass



      
class Coffe(Bevarages):
    def getCoffeePrice(self) -> int:
        return 102
    def getCoffeeDescribtion(self) -> str:
        return "Base Coffee"

class AddonDecrater(Bevarages):
    def __init__(self, beverage: Bevarages): 
        self.beverage = beverage
    
    def getCoffeePrice(self) -> int:
        return self.beverage.getCoffeePrice()
        
    def getCoffeeDescribtion(self) -> str:
        return self.beverage.getCoffeeDescribtion()    



class MilkwithCofee(AddonDecrater):
    def getCoffeePrice(self) -> int:
        return self.beverage.getCoffeePrice() + 12  # Fixed: Call getCoffeePrice() with ()
        
    def getCoffeeDescribtion(self) -> str:
        return self.beverage.getCoffeeDescribtion() + " + milk added"  # Fixed: Call getCoffeeDescribtion() with ()
class MilkwithCofeeandCoclate(AddonDecrater):
      def getCoffeePrice(self)->int:
            return self.beverage.getCoffeePrice() + 120 
      def getCoffeeDescribtion(self)->str:
            return self.beverage.getCoffeeDescribtion() + " milk and cholate added  add"




cooffe = Coffe()
milkedCofee = MilkwithCofee(cooffe)
# Stacking decorators: adding chocolate on top of the milked coffee
cocoCofee = MilkwithCofeeandCoclate(milkedCofee) 

print(cocoCofee.getCoffeeDescribtion())
print(cocoCofee.getCoffeePrice())