# 定义员工类
class Employee:
    def work(self):
        print("员工需要努力搬砖哦！")


# 定义经理类
class Manager(Employee):
    def work(self):
        print("开个早会")
        # 调用父类函数方式一：父类.需要调用的函数(self, 其他参数)
        # Employee.work(self)

        # 调用父类函数方式二：super(当前类, self).需要调用的函数(其他参数)
        # super(Manager, self).work()

        # 调用父类函数方式三：super().需要调用的函数(其他参数)
        super().work()

        print("开个晚会")


# 使用子类对象，调用功能
m = Manager()
m.work()
