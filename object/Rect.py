# 定义一个矩形类
class Rect:
    # 完成属性的初始化赋值
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # 计算面积
    def getArea(self):
        return self.length * self.width

    # 完成两个矩形的面积比较
    def __gt__(self, other):
        return self.getArea() > other.getArea()

    def __lt__(self, other):
        return self.getArea() < other.getArea()

    def __ge__(self, other):
        return self.getArea() >= other.getArea()

    def __le__(self, other):
        return self.getArea() <= other.getArea()

    def __eq__(self, other):
        return self.getArea() == self.getArea()

    def __ne__(self, other):
        return self.getArea() != self.getArea()

    # 将一个矩形转为字符串表示形式
    def __str__(self):
        return f"length: {self.length}, width: {self.width}, area: {self.getArea()}"
