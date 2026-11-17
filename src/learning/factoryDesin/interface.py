from abc import ABC, abstractmethod

# --- 1. ABSTRACT PRODUCTS ---
class Chair(ABC):
    @abstractmethod
    def sit_on(self) -> str:
        pass

class Sofa(ABC):
    @abstractmethod
    def lie_on(self) -> str:
        pass

# --- 2. CONCRETE PRODUCTS (Family 1: Modern) ---
class ModernChair(Chair):
    def sit_on(self) -> str:
        return "Sitting on a sleek modern chair."

class ModernSofa(Sofa):
    def lie_on(self) -> str:
        return "Lying on a minimalist modern sofa."


# --- 3. CONCRETE PRODUCTS (Family 2: Victorian) ---
class VictorianChair(Chair):
    def sit_on(self) -> str:
        return "Sitting on an elegant, carved Victorian chair."

class VictorianSofa(Sofa):
    def lie_on(self) -> str:
        return "Lying on a luxurious velvet Victorian sofa."


# --- 4. ABSTRACT FACTORY ---
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass
    
    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass

# --- 5. CONCRETE FACTORIES ---
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()
    
    def create_sofa(self) -> Sofa:
        return ModernSofa()

class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()
    
    def create_sofa(self) -> Sofa:
        return VictorianSofa()      


  # --- CLIENT CODE ---
def order_furniture(factory: FurnitureFactory):
    chair = factory.create_chair()
    sofa = factory.create_sofa()
    
    print(chair.sit_on())
    print(sofa.lie_on())


# --- TESTING ---
print("--- Ordering Modern Style ---")
modern_factory = ModernFurnitureFactory()
order_furniture(modern_factory)

print("\n--- Ordering Victorian Style ---")
victorian_factory = VictorianFurnitureFactory()
order_furniture(victorian_factory)            