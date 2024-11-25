from urllib.request import urlopen


# for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
#     line = line.decode('utf-8')  # Decoding the binary data to text.
#     if 'EST' in line or 'EDT' in line:  # look for Eastern Time
#         print(line)


def toSum(num):
    if num == 1:
        return 1
    else:
        return num + toSum(num - 1)


sum = toSum(100)
print(sum)


def test():
    return 1
    return 2


num = test()
print(num)


def show2(x, y=10):
    res = x + y
    print(f"x={x},y={y},res={res}")
    print(f"{x}+{y}的和是：{res}")


show2(1)
show2(1, 2)


def test_func(add):
    res = add(1, 2)
    print(f"计算结果为：{res}")


# 使用def和使用lambda，定义的函数功能完全一致，只是lambda关键字定义的函数是匿名的，无法二次使用
test_func(lambda x, y: x + y)
test_func(lambda x, y: x - y)


def func(x):
    def inner(y):
        return x + y

    return inner


f = func(2)
print(f)
print(f(8))
print(func(2)(8))


def outer(num):
    a = num
    b = 10
    print("a:", a)

    def inner():
        nonlocal a
        a += b
        print("outer a:", a)

    return inner

fn1 = outer(10)
fn1()