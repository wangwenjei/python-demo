from flask import Flask, render_template, request
from api import askChatGPT

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
        return askChatGPT(question=question)

    if request.method == 'POST':
        question = request.form.get('que')
        return askChatGPT(question=question)


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=6000, debug=True)
    app.run()
    # app.run(host='0.0.0.0', port=6000)
