from flask import Flask,request

app = Flask(__name__)


# 当前URL既可以支持GET请求,也可以支持POST请求,如果不写默认只能支持GET请求
@app.route('/index/', methods=['GET', 'POST'])
def index():
    print(request.form)  # 获取form表单提交过来的非文件数据
    # ImmutableMultiDict([('username', 'Jason'), ('password', '123'), ('birthday', '2021-08-27'), ('gender', 'male'), ('hobby', 'listen music'), ('hobby', 'Python'), ('my_file', '1.png'), ('my_info', 'hahaha')])

    print(request.files)  # 获取文件数据
    # ImmutableMultiDict([('my_file', <FileStorage: '1.png' ('image/png')>)])

    file_obj = request.files.get('my_file')
    file_obj.save(file_obj.name)
    return 'OK'


app.run()



""""

from flask import Flask, request


app = Flask(__name__)


# 当前url既可以支持get请求也可以支持post请求  如果不写默认只能支持get请求
@app.route('/index/',methods=['GET','POST'])
def index():
    print(request.form)  # 获取form表单提交过来的非文件数据
    # ImmutableMultiDict([('username', 'jason'), ('password', '123132131231233'), ('gender', 'on')])
    print(request.files)  # 获取文件数据
    file_obj = request.files.get('myfile.png')
    file_obj.save(file_obj.name)
    return 'OK'


app.run()
"""