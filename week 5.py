# Base class for movement (for polymorphism)
class Movement:
    def move(self):
        pass

# Specific movement types
class Flying(Movement):
    def move(self):
        return "Flying in the air! "

class Running(Movement):
    def move(self):
        return "Running super fast!"

# Base Superhero class
class Superhero:
    def __init__(self, name, power):
        self._name = name  
        self._power = power
        self._movement = None  

    def get_name(self):
        return self._name

    def show_info(self):
        return f"Name: {self._name}, Power: {self._power}"

    def use_power(self):
        return f"{self._name} uses a basic power!"

    def move(self):
        return f"{self._name} is {self._movement.move()}"

# Flying superhero subclass
class SkyHero(Superhero):
    def __init__(self, name, power):
        super().__init__(name, power)
        self._movement = Flying()

    def use_power(self):
        return f"{self._name} shoots energy from the sky!"

# Speedster superhero subclass
class SpeedHero(Superhero):
    def __init__(self, name, power):
        super().__init__(name, power)
        self._movement = Running()

    def use_power(self):
        return f"{self._name} dashes with speed!"

# Main program
def main():
    sky = SkyHero("Skyhawk", 80)
    speed = SpeedHero("Blaze", 85)
    
    for hero in [sky, speed]:
        print(hero.show_info())
        print(hero.use_power())
        print(hero.move())
        print("-" * 20)

if __name__ == "__main__":
    main()