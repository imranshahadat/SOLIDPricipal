class CoffeeOrder:
    def __init__(self):
        self.type = "Black Coffee"
        self.size = "Medium"
        self.milk = False
        self.sugar = 0

    def set_type(self, coffee_type: str):
        self.type = coffee_type
        return self  # Return self so we can chain the next method

    def set_size(self, size: str):
        self.size = size
        return self  # Return self

    def add_milk(self):
        self.milk = True
        return self  # Return self

    def add_sugar(self, spoons: int):
        self.sugar = spoons
        return self  # Return self

    def brew(self):
        milk_status = "with milk" if self.milk else "black"
        print(f"Brewing a {self.size} {self.type} ({milk_status}) with {self.sugar} spoon(s) of sugar.")
        return self


# --- USAGE (Method Chaining in Action) ---

# Instead of writing multiple separate lines, we chain them together like a sentence!
CoffeeOrder() \
    .set_type("Cappuccino") \
    .set_size("Large") \
    .add_milk() \
    .add_sugar(2) \
    .brew()