import numpy as np
from scipy.optimize import fsolve


# 定义方程 f(x) = 13^x - 12^x - 25
def equation(x):
    return 13 ** x - 12 ** x - 25


if __name__ == '__main__':
    # 使用 fsolve 来求解方程，猜测初始解为 x = 2
    x_initial_guess = 2
    solution = fsolve(equation, x_initial_guess)
    print(f"x 的值为: {solution[0]}")
