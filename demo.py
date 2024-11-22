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


if __name__ == '__main__':
    # fib(10)
    # printRange()
    # printRange2()
    forTest("apple2")
