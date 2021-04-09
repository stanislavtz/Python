# from point import Point
from sys import maxsize
from math import sqrt

def calculate_distance(p1, p2):
    x = abs(p1.x - p2.x)
    y = abs(p1.y - p2.y)
    return sqrt(x**2 + y**2)

class Point:
    def __init__(self, x, y):
        self.__x = self.set_x(x)
        self.__y = self.set_y(y)

    
    def set_x(self, x):
        if isinstance(x, float):
            return x
        raise Exception
    
    def set_y(self, y):
        if isinstance(y, float):
            return y
        raise Exception

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y




n = int(input())
points = []
min_distance = maxsize
for _ in range(n):
    data = list(map(float, input().split()))
    points.append(Point(data[0], data[1]))

for i in range(n-1):
    distance = calculate_distance(points[i], points[i+1])
    if distance < min_distance:
        min_distance = distance
