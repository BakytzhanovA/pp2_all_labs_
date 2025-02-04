class Shape:
    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Пример использования:
rectangle = Rectangle(5, 3)
print("Площадь прямоугольника:", rectangle.area())