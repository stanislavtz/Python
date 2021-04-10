class Rectangle:
    def __init__(self, data):
        self.uper_left = (self.set_data(data)[0], self.set_data(data)[1])
        self.lower_right = \
            (self.set_data(data)[0] + self.set_data(data)[2], self.set_data(data)[1] + self.set_data(data)[3])

    def set_data(self, data):
        if len(data) != 4:
            raise Exception

        return data


def compare_rectangles(r1, r2):
    if r1.uper_left >= r2.uper_left and r1.lower_right <= r2.lower_right:
        return 'Inside'
    return 'Not inside'


try:
    r1_data = list(map(float, input().split()))
    r2_data = list(map(float, input().split()))
except:
    print('data is invalid!')

r1 = Rectangle(r1_data)
r2 = Rectangle(r2_data)

print(compare_rectangles(r1, r2))