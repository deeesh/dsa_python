# Class properties of circle
class CircleProperties:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
    
    def area_of_circle(self):
        return self.pi * self.radius * self.radius

    def circumference(self):
        return 2 * self.pi * self.radius

area = CircleProperties(4)
print(area.area_of_circle())
print(area.circumference())
area = CircleProperties(14)
print(area.area_of_circle())
print(area.circumference())

#  Rectangle Properties with respect to class
class RectangeleProperties:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length * self.breadth
    
    def circum(self):
        return 2 * (self.length + self.breadth)
    
rect1 = RectangeleProperties(3, 4)
print(rect1.area())
print(rect1.circum())
rect2 = RectangeleProperties(30, 40)
print(rect2.area())
print(rect2.circum())

