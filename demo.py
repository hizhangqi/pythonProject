import sys  # 引入 sys 模块


# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
def fib(n):
    a, b = 0, 1
    while a < n:
        print(b, end=' ')
        a, b = b, a + b
    print()


def printRange2():
    for i in range(0, 5):
        # 第一个循环打印空格
        for m in range(0, i):
            print(" ", end=" ")
        # 打印 *
        """
         i  数量 = 9-2i
         0  9   
         1  7
         2  5
         3  3
         4  1
        """
        for n in range(0, 9 - 2 * i):
            print("*", end=" ")
        print()


def printRange():
    for i in range(9, 0, -2):
        # 打印空格的数量
        print(" " * (9 - i), end="")
        # 打印*的数量
        print("* " * i, end="")
        # 换行
        print()


def forTest(fruitSelect):
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        if fruit == fruitSelect:
            print(fruitSelect + " found")
            break
    else:
        print(fruitSelect + " not found")


def done():
    print()


def iterTest():
    list = [1, 2, 3, 4]
    it = iter(list)  # 创建迭代器对象
    print(next(it))  # 输出迭代器的下一个元素
    for x in it:
        print(x, end=" ")

    list = [1, 2, 3, 4]
    it = iter(list)  # 创建迭代器对象
    while True:
        try:
            print(next(it))
        except StopIteration:
            sys.exit()


def arithmetic_mean(*args):
    if len(args) == 0:
        return 0
    else:
        sum = 0
        for x in args:
            sum += x
        return sum / len(args)


print(arithmetic_mean(45, 32, 89, 78))
print(arithmetic_mean(8989.8, 78787.78, 3453, 78778.73))
print(arithmetic_mean(45, 32))
print(arithmetic_mean(45))
print(arithmetic_mean())

if __name__ == '__main__':
    done()
    # fib(10)
    # printRange()
    # printRange2()
    # forTest("apple2")
