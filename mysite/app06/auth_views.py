from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# python3 manage.py createsuperuser 创建管理员用户
# json 123

def auth_login(request):
    # if request.method == 'POST':
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # authenticate方法可以自动比较用户名和密码是否一致
        user_obj = auth.authenticate(request, username=username, password=password)
        # print(user_obj)  # 验证成功返回用户对象 ,失败返回None
        # print(user_obj.__dict__)

        if user_obj:
            # 保存用户状态;主要执行了该方法 你就可以在任何地方通过request.user获取到当前登陆的用户对象
            auth.login(request, user_obj)  # 类似于request.session[key] = user_obj
            return redirect('/app06/auth_home/')

    return render(request, 'app06/auth_login.html')


"""
局部配置
    @login_required(login_url='/app06/auth_login')
全局配置
    在settings文件中通过配置LOGIN_URL使其生效
总结:
    1.如果全局和局部同时配置,那么局部的优先级大于全局
    2.全局的好处是减少重复代码,但是跳转页面单一
      局部的好处是跳转灵活但需要单独指定

"""


# @login_required(login_url='/app06/auth_login')
@login_required
def auth_home(request):
    print(request.user)  # jason  如果没有登录返回 AnonymousUser匿名用户
    # 判断用户是否登录 Django1.x is_authenticated() 需要加括号
    print(request.user.is_authenticated)

    return HttpResponse('auth_home')


@login_required
def auth_set_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('oldPassword')
        new_password = request.POST.get('newPassword')
        confirm_password = request.POST.get('confirmPassword')

        # 校验输入的旧密码加密后是否与数据库一致
        is_right = request.user.check_password(old_password)
        if new_password == confirm_password and is_right:
            request.user.set_password(new_password)  # 仅仅只是修改对象属性
            request.user.save()  # 正真的操作数据库保存数据
            return redirect('/app06/auth_login')

    return render(request, 'app06/auth_set_password.html', locals())


@login_required
def auth_logout(request):
    auth.logout(request)  # 类似于 request.session.flush()
    return redirect('/app06/auth_login/')


def auth_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 创建普通用户;成功返回的是用户对象,重复会报错
        # res = User.objects.create_user(username=username, password=password)
        # res = User.objects.create_superuser(username=username, password=password)

        from app06.models import UserInfo
        res = UserInfo.objects.create_superuser(username=username, password=password, phone=18211111111)

    return render(request, 'app06/auth_register.html')
