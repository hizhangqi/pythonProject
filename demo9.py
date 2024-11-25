#!/usr/bin/python3
# 第二步：编写一个函数，判断是否为闰年
def is_leap(year):
    # 能被4整除，不能被100整除，或者只能被400整除的
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


# 根据年月获取每个月的天数
def getDayOfMonth(year, month):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif is_leap(year):
        return 29
    else:
        return 28


# 主函数，是入口，用于展示整个过程
def showMainScreen():
    # 第一步：输入一些数据
    year = int(input("请输入要查看的年份:"))
    month = int(input("请输入要查看的月份："))
    year_days = 0  # 年份的总天数
    month_days = 0  # 年份的总天数

    initYear = 1900
    while initYear < year:
        if is_leap(initYear):
            year_days += 366
        else:
            year_days += 365
        initYear += 1
    initMonth = 1
    # 2000 8
    while initMonth < month:
        month_days += getDayOfMonth(year, initMonth)
        initMonth += 1
    # 计算这个月份的第一天是星期几，假如是0表示星期日
    week = (year_days + month_days + 1) % 7
    print(week)

    # 接着开始打印万年历
    print("星期日\t\t星期一\t\t星期二\t\t星期三\t\t星期四\t\t星期五\t\t星期六")
    # 搞一个计数器，这个计数器的作用是换行
    counter = week
    # 打印空格的数量
    print("\t" * 3 * week, end="")
    # 打印 日期 ,有多少天就需要打印多少次
    monthofDay = getDayOfMonth(year, month)
    i = 1
    while i <= monthofDay:
        # 打印日期
        print(i, end="\t\t\t")
        # 打印换行
        if counter % 7 == 6 and counter != 0:
            print()
        counter += 1
        i += 1


showMainScreen()
