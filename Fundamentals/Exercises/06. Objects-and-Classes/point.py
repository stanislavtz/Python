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