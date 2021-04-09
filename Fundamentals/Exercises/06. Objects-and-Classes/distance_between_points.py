from math import sqrt

def calculate_distance(p1, p2):
    x = abs(p1.get_x() - p2.get_x())
    y = abs(p1.get_y() - p2.get_y())

    return sqrt(x**2 + y**2)

class Point:
    def __init__(self, x, y):
        self.__x = self.set_x(x)
        self.__y = self.set_y(y)
    
    def set_x(self, x):
        if not isinstance(x, float):
            raise Exception
        return x
    
    def set_y(self, y):
        if not isinstance(y, float):
            raise Exception
        return y

    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y

f_p_coords = input().split()
s_p_coords = input().split()

p1 = Point(float(f_p_coords[0]), float(f_p_coords[1]))
p2 = Point(float(s_p_coords[0]), float(s_p_coords[1]))

print(f'{calculate_distance(p1, p2):.3f}')