# 使用关键字class定义一个类
class Dog:
    def __init__(self):
        # 使用self.定义属性
        self.name = None
        self.age = None
        self.kind = None

    # 定义对象的行为，用方法来定义，又称为“成员方法”
    # 成员方法的定义，参数必需添加self，表示对象本身
    def bark(self):
        # 在方法中，使用self.访问对象自己的属性和方法
        print(f"{self.name} 在狗叫")


# 实例化对象
xiaobai = Dog()

# 访问类的属性
xiaobai.name = "xiaobai"
xiaobai.age = 1
print(xiaobai.name)
print(xiaobai.age)

# 访问类的方法
xiaobai.bark()
