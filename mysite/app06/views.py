import requests
from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.utils.decorators import method_decorator

# Create your views here.
""" cookie方式 """


def login_auth(func):
    def inner(request, *args, **kwargs):
        target_url = request.get_full_path()  # 获取用户url实现用户之前访问什么页面,登录后自动访问该页面
        if request.COOKIES.get('username'):  # request.COOKIE.get(key)  获取cookie
            return func(request, *args, **kwargs)
        else:
            return redirect('/app06/login/?next=%s' % target_url)

    return inner


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'Jason' and password == '123':
            """
                当 target_url 有值时访问用户想要访问的页面,
                当为None时给一个默认登录成功后的访问页面 
            """
            target_url = request.GET.get('next')
            if target_url:
                obj = redirect(target_url)
            else:
                obj = redirect('/app06/home/')

            # 添加cookie信息 max_age过期时间单位为秒
            obj.set_cookie('username', 'jason_cookie', max_age=7200, )
            return obj

    return render(request, 'app06/login.html')


@login_auth
def home(request):
    # if request.COOKIES.get('username'):
    #     return HttpResponse('我是home页面，只有登陆的用户才能进来哟~')
    # else:
    #     return render(request, 'app06/login.html')
    return HttpResponse('我是home页面，只有登陆的用户才能进来哟~')


@login_auth
def index(request):
    return HttpResponse('我是index页面，只有登陆的用户才能进来哟~')


@login_auth
def logout(request):
    obj = redirect('/app06/login/')
    # 删除cookie
    obj.delete_cookie('username')
    return obj


"""  session方式 """


def login_auth_2(func):
    def inner(request, *args, **kwargs):
        target_url = request.get_full_path()  # 获取用户输入的URL
        if request.session.get('username'):  # request.session.get(key) 获取session
            return func(request, *args, **kwargs)
        else:
            return redirect('/app06/mylogin/?next=%s' % target_url)

    return inner


class MyLogin(View):
    def get(self, request):
        return render(request, 'app06/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'Jason' and password == '123':
            # 添加session信息
            request.session['username'] = username
            # 设置session超时时间,可放整数单位为秒,还可以放时间对象,不写则取决于Django默认的session超时时间14天
            request.session.set_expiry(7200)
            target_url = request.GET.get('next')
            if target_url:
                return redirect(target_url)
            else:
                return redirect('/app06/myhome/')

        return render(request, 'app06/login.html')


@method_decorator(login_auth_2, name='get')  # CBV使用装饰器方式一: 指名道姓使用,可以添加多个针对不同的方法加不同的装饰器
@method_decorator(login_auth_2, name='post')
class MyHome(View):
    def get(self, request):
        return HttpResponse('我是home页面，只有登陆的用户才能进来哟~session')

    def post(self, request):
        # if request.session.get('username'):
        #     return HttpResponse('我是home页面，只有登陆的用户才能进来哟~session')
        # else:
        #     return render(request, 'app06/login.html')

        return HttpResponse('我是home页面，只有登陆的用户才能进来哟~session')


class MyIndex(View):
    @method_decorator(login_auth_2)  # CBV使用装饰器方式二: 指名道姓的使用
    def get(self, request):
        return HttpResponse('我是index页面，只有登陆的用户才能进来哟~session')

    @method_decorator(login_auth_2)
    def post(self, request):
        return HttpResponse('我是index页面，只有登陆的用户才能进来哟~session')


class MyLogout(View):
    @method_decorator(login_auth_2)  # CBV使用装饰器方式三: 会直接作用于当前类里面所有的方法
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        # request.session.delete() # 只删除服务端session记录,客户端不删除
        request.session.flush()  # 客户端服务端都清除,推荐使用
        return redirect('/app06/mylogin/')


def set_session(request):
    # 添加了多个session键值对但是在django_session表中只有一条数据
    request.session['hobby'] = 'basketball'
    request.session['hobby1'] = 'football'
    request.session['hobby2'] = 'music'
    return HttpResponse('添加session')


def get_session(request):
    # session是一个对象,可以获取到其中某个session
    if request.session.get('hobby'):
        print(request.session)
        print(request.session.get('hobby'))
        print(request.session.get('hobby1'))
        print(request.session.get('hobby2'))
        return HttpResponse('成功获取session')
    return HttpResponse('获取session失败咯')
