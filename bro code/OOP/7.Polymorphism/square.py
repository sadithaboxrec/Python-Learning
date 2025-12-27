from shape import Shape

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2