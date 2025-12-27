# multiple inheritance = inherit from more than one parent class
#                           C(A,B)

#  multilevel inheritance = inherit from a parent which inherits from another account
#                           C(B) <- B(A)  <- A


class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


# Multilevel inheritance
#     Animal is Grand Parent
#     Prey,Predator is Parent and Fish,Hawk,Rabbit are sub classes


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

# multiple inheritance
class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs Bunny")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.flee()
# rabbit.hunt()
rabbit.sleep()

hawk.hunt()
# hawk.flee()
hawk.eat()

fish.hunt()
fish.flee()
fish.sleep()
fish.eat()