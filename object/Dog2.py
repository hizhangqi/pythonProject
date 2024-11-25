# 使用关键字class定义一个类
class Dog:
    # __init__是初始化对象的时候自动调用的方法，称为“构造方法”
    # 在构造方法中，也可以完成属性的定义与初始化赋值操作
    def __init__(self, name, age, kind):
        # 使用self.定义属性，后面直接使用形参完成初始化赋值
        self.name = name
        self.age = age
        self.kind = kind

    # 定义对象的行为，用方法来定义
    # 成员方法的定义，参数必需添加self，表示对象本身
    def bark(self):
        # 在方法中，使用self.访问对象自己的属性和方法
        print(f"{self.name} 在狗叫")


# 实例化对象
xiaobai = Dog("xiaobai", 1, "samo")

# 访问类的属性
print(xiaobai.name)
print(xiaobai.age)

# 访问类的方法
xiaobai.bark()
