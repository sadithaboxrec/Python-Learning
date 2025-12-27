# Inheritance = Inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#                class Child(Parent)
#                class sub(Super Classes)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is asleep")

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

print(dog.name)
print(dog.is_alive)
print(dog.eat())
print(dog.speak())
print()
print(cat.name)
print(cat.is_alive)
print(cat.speak())
