try:
    # 让用户在控制台输入数字，输入的可能不正确
    number = int(input("please input a number: "))
except ValueError as v:
    print("输入的不是数字！")
else:
    print("用户的输入没有问题")
finally:
    print("finally")


# try:
#     # 让用户在控制台输入数字，输入的可能不正确
#     number = int(input("please input a number: "))
# except ValueError as v:
#     print("输入的不是数字！")
# finally:
#     print("finally")