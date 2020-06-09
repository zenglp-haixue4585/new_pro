from flask import Flask, jsonfy, request
import pymysql
from test import DoMysql

method_err = {
    "code": 301,
    "msg": "请求方法不正确"
}

param_err = {
    "code": 302,
    "msg": "请求参数错误"
}

money_err = {
    "code": 303,
    "msg": "账户余额不足"
}

price_err = {
    "code": 304,
    "msg": "价格不合法"
}

user_err = {
    "code": 305,
    "msg": ""
}

db_err = {
    "code": 306,
    "msg": "数据库异常"
}
success_msg = {
    "code": 200,
    "msg": "支付成功"
}


def check_float(string):
    """
    判断输入数据为小数
    :param string:
    :return:
    """
    str1 = str(string)
    if str1.count(".") > 1:
        return False
    elif str1.count("-") > 0:
        return False
    elif str1.isdigit():
        return False
    else:
        new_str = str1.split(".")
        first_num = new_str[0]
        if first_num.isdigit() and new_str[1].isdigit():
            return True
        else:
            return False


def check_balance(user_id, price):
    """
    检查账户余额
    :param user_id:
    :param price:
    :return:
    """
    try:
        my_db = DoMysql()

    except Exception as e:
        print("连接异常：", e)
        return db_err
    else:
        select_sql = f'select money from accounts where user_id = {user_id}'
        data = my_db.fetchall(select_sql)
        if data:
            money = data[0]
            if money >= price:
                target_money = money - price
                update_sql = f'update accounts set money = {target_money} where user_id = {user_id} '
                my_db.fetchone(update_sql)
                my_db.close()
                return success_msg
            else:
                return money_err
        else:
            return user_err


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


@app.route("/", methods=["GET", "POST"])
def pay():
    if request.method != "POST":
        return jsonfy(method_err)
    else:
        user_id = request.values.get("user_id")
        price = request.values.get("price")
        if user_id and price:
            if price.isdigit():
                price = int(price)
            elif check_float(price):
                price = float(price)
            else:
                return jsonfy(param_err)
            res = check_balance(user_id, price)
            return jsonfy(res)
        else:
            return jsonfy(param_err)


if __name__ == '__main__':
    app.run(debug=True)
