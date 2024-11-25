"""
案例: 上课了，老师让学生做自我介绍
分析:
    1、需要设计两个类: 老师类 和 学生类
    2、老师类的功能: 让学生做自我介绍
    3、学生类的功能: 自我介绍
"""


class Student:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def showSelf(self):
        print(f"我叫{self.name},来自于{self.city},欢迎来我的家乡做客")


class Teacher:
    def __init__(self, name):
        self.name = name

    def tiWen(self, stu: Student):
        print("现在有请%s做自我介绍" % stu.name)
        stu.showSelf()


teacher = Teacher("张老师")
student = Student("张自力同学", "洛阳嵩县")
teacher.tiWen(student)

from object.Point import Point
p1 = Point(1, 2)
print(p1)