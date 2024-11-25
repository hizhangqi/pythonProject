import pymysql


class PayError(Exception):
    pass


def pay(from_account, to_account, money):
    # 建立数据库连接
    db_connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="mysqlmysql",
        database="test1"
    )
    # 增删改查的过程
    # 它是执行 SQL语句的对象 获取光标对象
    db_cursor = db_connection.cursor()
    try:
        # 检查付款账号是否存在
        res1 = db_cursor.execute("select * from bank_account where user_name = %s", from_account)
        if res1 == 0:
            raise PayError("付款账号不存在")

        # 检查余额是否足够
        rest_money = db_cursor.fetchone()[2]
        if rest_money < money:
            raise PayError("账号余额不足")

        # 检查转入账号是否存在
        res2 = db_cursor.execute("select * from bank_account where user_name = %s", to_account)
        if res2 == 0:
            raise PayError("转入账号不存在")

        sql1 = "update bank_account set account_balance=account_balance-%s where user_name=%s"
        db_cursor.execute(sql1, (money, from_account))
        a = 10 / 0
        sql2 = "update bank_account set account_balance=account_balance+%s where user_name=%s"
        db_cursor.execute(sql2, (money, to_account))

        # 成功就提交
        db_connection.commit()
    except Exception as e:
        print(e)
        print("转账失败")

        # 失败就回滚
        db_connection.rollback()
    finally:
        db_cursor.close()
        db_connection.close()


from_account = input("请输入需要付款的账号名: ")
to_account = input("请输入需要收款的账号名: ")
money = float(input("请输入需要转账的金额: "))

pay(from_account, to_account, money)
