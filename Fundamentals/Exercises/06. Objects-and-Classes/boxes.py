import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * self.width + 2 * self.height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Box: {self.width:.0f}, {self.height:.0f}\nPerimeter: {self.perimeter():.0f}\nArea: {self.area():.0f}"

class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    
def calculate_distance(p1, p2):
    return math.sqrt(abs(p1.x - p2.x)**2 + abs(p1.y - p2.y)**2)

rectangles = []
data = input()
while data != 'end':
    points_coords = data.split(' | ')
    point_a = Point(points_coords[0].split(':')[0], points_coords[0].split(':')[1])
    point_b = Point(points_coords[1].split(':')[0], points_coords[1].split(':')[1])
    point_c = Point(points_coords[2].split(':')[0], points_coords[2].split(':')[1])
    point_d = Point(points_coords[3].split(':')[0], points_coords[3].split(':')[1])

    width = calculate_distance(point_a, point_b)
    height = calculate_distance(point_a, point_c)

    rectangle = Rectangle(width, height)
    rectangles.append(rectangle)
    data = input()

for rec in rectangles:
    print(rec)