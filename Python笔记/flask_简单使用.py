from flask import Flask, jsonify

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # jsonify返回的中文正常显示

data = [
    {"id": 1, "username": "小明", "password": "123456", "role": 0, "sex": 0, "telephone": "10086", "address": "北京市海淀区"},
    {"id": 2, "username": "李华", "password": "abc", "role": 1, "sex": 0, "telephone": "10010", "address": "广州市天河区"},
    {"id": 3, "username": "大白", "password": "666666", "role": 0, "sex": 1, "telephone": "10000", "address": "深圳市南山区"}
]


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/users", methods=["GET"])
def get_all_users():
    """获取所有用户信息"""
    return jsonify({"code": "0", "data": data, "msg": "操作成功"})


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    """获取某个用户信息"""
    if user_id > 0 and user_id <= len(data):
        return jsonify({"code": "0", "data": data[user_id - 1], "msg": "操作成功"})
    return jsonify({"code": "1", "msg": "用户不存在"})


"""
http://127.0.0.1:5000/users/1
    ===> {"code":"0","data":{"address":"北京市海淀区","id":1,"password":"123456","role":0,"sex":0,"telephone":"10086","username":"小明"},"msg":"操作成功"}
"""

if __name__ == '__main__':
    app.run()
