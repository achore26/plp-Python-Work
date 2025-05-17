class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def get_specs(self):
        return f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB"

class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, cooling_system):
        super().__init__(brand, model, storage)
        self.cooling_system = cooling_system

    def get_specs(self):
        base_specs = super().get_specs()
        return base_specs + f", Cooling System: {self.cooling_system}"

    def launch_game(self, game_name):
        print(f"Launching {game_name} on {self.model}... Ready to play!")

phone1 = Smartphone("Samsung", "Galaxy S21", 128)
gaming_phone1 = GamingPhone("Asus", "ROG Phone 5", 256, "Vapor Chamber")

print(phone1.get_specs())
phone1.call("123-456-7890")

print(gaming_phone1.get_specs())
gaming_phone1.launch_game("PUBG")
------------------------------------------------------------------------------
class Animal:
    def move(self):
        print("Animal is moving...")

class Dog(Animal):
    def move(self):
        print("Dog is running 🐶")

class Fish(Animal):
    def move(self):
        print("Fish is swimming 🐟")

class Bird(Animal):
    def move(self):
        print("Bird is flying 🐦")

animals = [Dog(), Fish(), Bird()]

for animal in animals:
    animal.move()
