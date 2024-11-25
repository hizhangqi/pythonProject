#!/usr/bin/python3

# 关于__str__和__repr__
# __str__: 在使用str(obj)的时候触发
# __repr__: 官方的描述是返回对象的规范字符串表示形式
# 两者都是将对象转成字符串的。
# 如果是直接用print打印的话，会自动的调用str()方法，因此会触发__str__
# 但是如果需要透过容器看对象的时候，是以__repr__为准的
# 那么我们应该写__str__还是__repr__呢？
# 推荐__repr__，因为如果只定义了__repr__，没有定义__str__。此时__str__是与__repr__相同的！
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"str: name = {self.name}, age = {self.age}"

    def __repr__(self):
        return f"repr: name = {self.name}, age = {self.age}"


xiaobai = Person("xiaobai", 18)

# 直接打印
print(xiaobai)  # str: name = xiaobai, age = 18

# 放入容器
arr = [xiaobai]
print(arr)  # repr: name = xiaobai, age = 18

