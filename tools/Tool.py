class Tool:
    @staticmethod
    def get_sum(*args, **kwargs):
        # 将所有的数字合并到一个元组中
        data = args + tuple(kwargs.values())
        # 定义变量，用来记录累加的结果
        res = 0
        # 累加
        for ele in data:
            res += ele
        return res

    @staticmethod
    def is_prime_number(number):
        if number < 2:
            return False
        for i in range(2, (number // 2) + 1):
            if number % i == 0:
                return False
        return True


# 工具类的使用
print(Tool.get_sum(99, 100, 98, chinese=99, math=89, english=100, mysql=90, python=90))
print(Tool.is_prime_number(99))
