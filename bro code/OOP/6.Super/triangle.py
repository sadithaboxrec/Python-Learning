from shape import Shape

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height


        """
        Method Overriding
        
    # def describe(self):
    #     print(f"It is a triangle with an area of {self.width * self.height / 2}cm^2")
    
        """

    def describe(self):
        print(f"It is a triangle with an area of {self.width * self.height / 2}cm^2")
        super().describe()