"""
案例: 判断一个圆是否包含一个点
分析:
    需要设计的类: 圆类、点类

    点类需要设计的属性: x, y坐标
    圆类需要设计的属性: 圆心（点类型）, 半径
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, point: Point, radius: int):
        self.point = point
        self.radius = radius

    def isContains(self, point: Point):
        x_ping = pow(self.point.x - point.x, 2)
        y_ping = pow(self.point.y - point.y, 2)
        if (x_ping + y_ping) < pow(self.radius, 2):
            return True
        else:
            return False

    def __contains__(self, item):
        return self.isContains(item)


point = Point(2, 3)
point2 = Point(2, 2)
circle = Circle(point2, 5)

#
print(circle.isContains(point))

# __contains__ 在使用in 或者not in 的时候自动触发
print(point in circle)
