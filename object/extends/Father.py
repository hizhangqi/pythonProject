# 定义父类1
class Father:
    def test_function(self):
        print("father function impl")

    def test1(self):
        print("test1")


# 定义父类2
class Mother:
    def test_function(self):
        print("mother function impl")

    def test2(self):
        print("test2")


# 定义子类，同时继承自两个父类
class Son(Father, Mother):

    def test_function(self):
        # 调用父类中的实现，区分父类调用的时候，只能使用父类名字来区分
        # Father.test_function(self)
        Mother.test_function(self)


# 1. 由于Son有两个父类，因此可以继承到两个父类中的所有的成员
s = Son()
s.test1()  # test1
s.test2()  # test2

# 2. 但是子类的多个父类中，包含了相同的函数 test_function，并且实现的方式不同。那么子类该何去何从？该继承哪个父类中的函数呢？这样的问题就是"二义性"
#    Python作为一门多继承的编程语言，自然是考虑到这个问题了。在Python中，如果出现这种情况，继承到的是小括号中写的第一个类！
s.test_function()
