#Exercise with OOP
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y


total_points = []
for x in range(1, 11):
    total_points.append(Point(x, x ** 2))

for point in total_points:
    print(f"For x={point.get_x()} then y = {point.get_y()}")