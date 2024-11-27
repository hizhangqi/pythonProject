import sys


def func(x=1, y=2):
    x = x + y
    y += 1
    print(x, y)


if __name__ == '__main__':
    func(y=2, x=1);
    func(2, 1);


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


# 5*4*3*2*1=120

def ways(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return ways(n - 1) * ways(n - 2)


print(ways(4))
print(ways(5))

# hanoi 函数接收四个参数：盘子的数量 n，起始柱 source，辅助柱 auxiliary 和目标柱 target。
# 当 n 为1时，表示只有单个盘子，直接打印移动指令。
# 对于 n > 1 的情况，函数首先调用自身将 n-1 个盘子从起始柱移动到辅助柱，然后打印移动最大盘子的指令，最后再次调用自身将 n-1 个盘子从辅助柱移动到目标柱。
# 这种递归调用的方式有效地解决了汉诺塔问题，无论盘子的数量是多少。
def hanoi(n, source, auxiliary, target):
    """
    解决汉诺塔问题的递归函数。

    参数:
    n -- 盘子的数量
    source -- 起始柱
    auxiliary -- 辅助柱
    target -- 目标柱
    """
    if n == 1:
        # 基本情况：只有一个盘子，直接移动
        print(f"Move disk 1 from {source} to {target}")
    else:
        # 递归情况
        # 先将n-1个盘子从起始柱移动到辅助柱
        hanoi(n - 1, source, target, auxiliary)
        # 移动第n个盘子从起始柱到目标柱
        print(f"Move disk {n} from {source} to {target}")
        # 最后将n-1个盘子从辅助柱移动到目标柱
        hanoi(n - 1, auxiliary, source, target)


# 示例调用
hanoi(3, 'A', 'B', 'C')
