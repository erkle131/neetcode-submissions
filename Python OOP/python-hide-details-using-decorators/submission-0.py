class SuperHero:
    def __init__(self, name: str, health: int, power_level: int):
        self.name = name
        self.__health = health
        self.__power_level = power_level
    
    # TODO: Add the getter and setter methods

    # Getter
    @property
    def health(self) -> int:
        return self.__health

    @property
    def power_level(self) -> int:
        return self.__power_level
    # Remember to use the @property decorator for the getter methods
    # Remember to use the @setter decorator for the setter methods

    # Setter
    @health.setter
    def health(self, value) -> None:
        if value > 100:
            print("You can't set the health to more than 100")
            return
        elif value < 0:
            print("You can't set the health to less than 0")
            return
        self.__health = value

    @power_level.setter
    def power_level(self, value) -> None:
        if value > 10:
            print("You can't set the power level to more than 10")
            return
        elif value < 1:
            print("You can't set the power level to less than 1")
            return
        self.__power_level = value


# Don't change the following code
super_hero = SuperHero("Batman", 80, 9)

print(super_hero.health) # this should print 80
super_hero.health = 110 # this should print You can't set the health to more than 100

print(super_hero.power_level) # this should print 9
super_hero.power_level = 100 # this should print You can't set the power level to more than 10
super_hero.power_level = 0 # this should print You can't set the power level to less than 1


# TODO: print the hero's attributes 
print(f"{super_hero.name} has {super_hero.health} health and {super_hero.power_level} power level")