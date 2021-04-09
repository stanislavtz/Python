# from point import Point
import math
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
min_distance 
for _ in range(n):
    data = list(map(float, input().split()))
    points.append(Point(data[0], data[1]))

