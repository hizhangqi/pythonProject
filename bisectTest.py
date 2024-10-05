from scipy.optimize import bisect


# 定义方程 f(x) = 13^x - 12^x - 25
def equation(x):
    return 13 ** x - 12 ** x - 25


if __name__ == '__main__':
    # 使用 bisect 来在区间 [1, 3] 中搜索解
    solution = bisect(equation, 1, 3)

    print(f"x 的值为: {solution}")
