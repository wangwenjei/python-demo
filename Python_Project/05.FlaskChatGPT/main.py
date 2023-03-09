import requests
from flask import Flask, request
import json
import logging
from ChatGptApi import ChatGPT_turbo, ChatGPT_Picture
from WeChatMessage import WeChatMes

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        print(username)
        print(password)
        return u'POST' + '+' + username + '+' + password
    if request.method == "GET":
        print('call get now')
        username = request.args.get('username')
        password = request.args.get('password')
        print(username)
        print(password)
        return username


@app.route('/ChatGPT', methods=['POST', 'GET'])
def ChatGPT():
    if request.method == 'GET':
        question = request.args.get('que')
        return ChatGPT_turbo(question=question)

    if request.method == 'POST':
        back_dic = {'code': 200, 'msg': ''}
        question = request.get_data()
        question = question.decode('utf-8')
        question = json.loads(question).get('que').lstrip()

        if question is None or question == '':
            back_dic['code'] = 10001
            back_dic['msg'] = '提问不能为空'
            back_dic = json.dumps(back_dic, ensure_ascii=False)
            return back_dic

        question = question[-200:]
        app.logger.info(question)

        back_dic['msg'] = ChatGPT_turbo(question=question)
        back_dic = json.dumps(back_dic, ensure_ascii=False)
        return back_dic


@app.route('/ChatGPTpicture', methods=['POST', 'GET'])
def ChatGPTpicture():
    if request.method == 'GET':
        question = request.args.get('q')
        return ChatGPT_Picture(description=question)


@app.route('/Wx/Message', methods=['GET'])
def WxMessage():
    if request.method == 'GET':
        content = request.args.get('q')
        wechat = WeChatMes()
        wechat.send_message(content=content)
        return content


@app.route('/Wx/dataVerify', methods=['GET'])
def dataVerify():
    if request.method == 'GET':
        msg_signature = request.args.get('msg_signature')
        timestamp = request.args.get('timestamp')
        nonce = request.args.get('nonce')
        echostr = request.args.get('echostr')

        wechat = WeChatMes()
        msg = wechat.dataVerify(msg_signature=msg_signature,
                                timestamp=timestamp,
                                nonce=nonce,
                                echostr=echostr)
        return 'hello'


if __name__ == '__main__':
    app.debug = True
    handler = logging.FileHandler('log/flask.log', encoding='UTF-8')
    handler.setLevel(logging.DEBUG)  # 设置日志记录最低级别为DEBUG，低于DEBUG级别的日志记录会被忽略，不设置setLevel()则默认为NOTSET级别。
    logging_format = logging.Formatter('[%(asctime)s]  %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)

    # app.run()
    app.run(host='0.0.0.0', port=5000)
    # app.run(host='0.0.0.0', port=6000, debug=True)
