class Superhero:
    def __init__(self, name, power, universe):
        self.name = name
        self.power = power
        self.universe = universe

    def introduce(self):
        return f"I am {self.name} from {self.universe}, and my power is {self.power}!"

    def fight(self):
        return f"{self.name} uses {self.power} to fight evil!"

class Villain(Superhero):
    def __init__(self, name, power, universe, evil_plan):
        super().__init__(name, power, universe)
        self.evil_plan = evil_plan

    def fight(self):
        return f"{self.name} uses {self.power} to execute the evil plan: {self.evil_plan}!"

# Example usage:
hero = Superhero("Photon", "light manipulation", "Starverse")
villain = Villain("Darkshade", "shadow control", "Starverse", "Eclipse the Sun")

print(hero.introduce())
print(hero.fight())

print(villain.introduce())
print(villain.fight())

class Vehicle:
    def move(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

class Car(Vehicle):
    def move(self):
        return "Driving on the road"

class Plane(Vehicle):
    def move(self):
        return "Flying in the sky"

class Boat(Vehicle):
    def move(self):
        return "Sailing across the sea"

# Example usage
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    print(vehicle.move())

