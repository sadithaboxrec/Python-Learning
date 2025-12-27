'''
    "Duck typing" = Another way to achieve polymorphism besides Inheritance
    Object must have the minimum necessary attributes/methods
    "If it looks like a duck and quacks like a duck, it must be a duck."

'''

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")


# class Car:
#
#     def horn(self):
#         print("HONK!")


class Car:
    alive = False

    # in original car class didn't have the alive attribute, so it gave error in animal class iterate so we added it as a class variable
    # and now it satisfy the class  in duck typing matter

    def speak(self):
        print("HONK!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)