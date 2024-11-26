class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 1 <= age <= 150:
            self.__age = age
        else:
            raise ValueError("年龄异常")


p = Person(19, 200)
