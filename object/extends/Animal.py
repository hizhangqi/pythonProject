# 定义动物类，其中定义动物共有的属性和行为
# 属性使用成员变量来表示
# 行为使用函数来表示
class Animal:
    def __init__(self, name, age, gender):
        """
        Animal类的构造函数，实现实例化对象的同时，完成属性的初始化赋值操作
        :param name:
        :param age:
        :param gender:
        """
        self.name = name
        self.age = age
        self.gender = gender

    def bark(self):
        print("animal bark")

    def __repr__(self):
        return "Animal: {name = %s, age = %d, gender = %s}" % (self.name, self.age, self.gender)


# 定义动物的子类，Dog
# 在类的后面添加小括号，小括号中写父类
# 此时，Dog类继承自Animal类。Animal是父类、Dog是子类
class Dog(Animal):
    def walk(self):
        print(f"{self.name} 会走路了")


# 实例化Dog对象的时候，由于继承到的父类的构造函数中包含有三个参数，因此，Dog对象也必需使用三个参数的构造函数
d = Dog("xiaobai", 1, "male")
# 子类中虽然没有定义bark函数，但是仍然可以调用，因为可以从父类继承到
d.bark()
# 子类中虽然没有定义name、age、gender属性，但是仍然可以调用，因为可以从父类继承到
print(d.name)
print(d.age)
print(d.gender)
# 子类虽然没有写__repr__或者__str__，仍然可以调用，因为可以从父类继承到
print(d)

# 子类在继承到父类成员的同时，还可以自己添加功能
d.walk()
