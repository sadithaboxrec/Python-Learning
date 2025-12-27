
from car import Car

car1 = Car('BMW', 2022, 'blue', False)
car2 = Car('Toyota', 2025, 'blue', True)

print(car1.model)
print(car1.year)  # . known as attribute access operator
print(car1.color)
print(car1.for_sale)
print()
print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)
print()

car1.drive()
car1.stop()
car2.drive()
