from triangle import Triangle
from circle import Circle
from square import Square

circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="blue", is_filled=False, width=6)
triangle = Triangle(color="yellow", is_filled=True, width=7, height=8)


print(circle.color)
print(square.width)

circle.describe()
square.describe()
triangle.describe()