from django.shortcuts import render, HttpResponse, redirect
from app01 import models


# Create your views here.

def index(request):
    # return HttpResponse('Hello Django')   # 返回字符串
    # return render(request, 't1.html')     # 返回HTML页面
    # return redirect('http://www.baidu.com') # 跳转到一个外部的URL
    return redirect('/home/')  # 跳转到内部的一个URL,自动拼接  http://127.0.0.1/home/


def home(request):
    return HttpResponse('home')


def ab_render(request):
    user_dist = {'username': 'jasonwang', 'age': 18}
    # 方式一:
    # return render(request, 't1.html', {'data': user_dist, 'date': 123})
    # 方式二: 当你要传的数据特别多的时候
    "locals会将所在的名称空间中所有的名字全部传递给HTML页面"
    return render(request, 't1.html', locals())


# 登录
def login(request):
    """
        # print(request.method)  # 返回请求方式, 并且是全大写的字符串形式 <class 'str'>

        if request.method == 'GET':
            print('来了,来了')
            return render(request, 'blog.html')
        elif request.method == 'POST':
            return HttpResponse('收到 over')
    该方式相对于复杂,可简写成下面方式
    """
    """
    request 方法使用
    
    if request.method == 'POST':
        print(request.POST)  # <QueryDict: {'username': ['Administrator'], 'password': ['123']}>  键值对中键取决于前端传输时标签中的name属性,值是用户输入的
        return HttpResponse('收到 over')
    # 获取URL后面携带的参数 http://127.0.0.1:8000/login/?username=Jason&password=123&hobby=11&hobby=22&hobby=33
    print(request.GET)  # <QueryDict: {'username': ['Jason'], 'password': ['123'], 'hobby': ['11', '22', '33']}>
    print(request.GET.get('hobby'))
    print(request.GET.getlist('hobby'))
    return render(request, 'blog.html')
    """

    if request.method == 'POST':
        username = request.POST.get('username')
        passwd = int(request.POST.get('password'))

        from app01 import models
        # select * from app01_user where username = username
        # user_obj =  models.User.objects.filter(username=username)[0]
        user_obj = models.User.objects.filter(username=username).first()

        if user_obj:
            if passwd == user_obj.password:
                return HttpResponse('登录成功')
            else:
                return HttpResponse('密码错误')
        else:
            return HttpResponse("用户不存在")

    else:
        return render(request, 'login.html')


# 注册(增)
def reg(request):
    # print(request.POST)
    username = request.POST.get('username')
    passwd = request.POST.get('password')

    if request.method == 'POST':
        from app01 import models
        models.User.objects.create(username=username, password=passwd)

    return render(request, 'register.html')


# 获取所有用户列表(查)
def userlist(request):
    # 两种获取表中所有数据的方式,第二种语义更加明确推荐使用
    # res = models.User.objects.filter()
    user_questset = models.User.objects.all()

    return render(request, r'userlist.html', locals())


# 编辑用户数据(改)
def edit_user(request):
    # 获取URL问号后面的参数
    user_id = request.GET.get('user_id')

    # 查询当前用户想要编辑的数据对象
    edit_obj = models.User.objects.filter(id=user_id).first()

    if request.method == 'POST':
        # 获取用户需要修改的数据
        username = request.POST.get('username')
        passwd = request.POST.get('password')

        # 去数据库中修改
        # 修改数据方式一: 该方式是将 filter 查询出来的列表中所有的对象全部更新   是批量更新操作  只修改被修改的字段
        # models.User.objects.filter(id=user_id).update(username=username, password=passwd)

        # 修改数据方式二: 当字段特别多的时候效率会非常低, 因为他从头到尾 无论该字段是否被修改 都将数据的所有字段全部更新了一遍
        edit_obj.username = username
        edit_obj.password = passwd
        edit_obj.save()

        return redirect('/app01/userlist/')

    return render(request, r'edituser.html', locals())


def delete_user(request):
    delete_id = request.GET.get('user_id')
    # 批量删除
    models.User.objects.filter(id=delete_id).delete()

    return redirect(r'/app01/userlist/')


def roule001(request):
    return HttpResponse('this is app01 roule001')
