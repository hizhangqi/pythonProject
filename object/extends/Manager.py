class Employee:
    def __init__(self, empno, name, sal):
        self.empno = empno
        self.name = name
        self.sal = sal
        print("Employee.__init__")


class Manager(Employee):
    pass


# 子类中没有定义构造函数，对象在实例化的时候，需要使用从父类中继承到的构造函数
m = Manager(101, 'zhangsanfeng', 9900)  # Employee.__init__
