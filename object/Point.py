# 定义一个点类
class Point:
    # 完成属性的初始化赋值
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 完成两个点的相加，得到一个新的点
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # 完成两个点的相减，得到一个新的点
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # 判断两个点是否相等，通过属性值是否相等的判断
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # 判断两个点是否不等，通过属性值是否相等的判断
    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    # 判断一个点的x和y坐标中，是否包含指定的值
    def __contains__(self, elem):
        return elem == self.x or elem == self.y

    # 将一个点转为字符串表示形式
    def __str__(self):
        return "{%d, %d}" % (self.x, self.y)
