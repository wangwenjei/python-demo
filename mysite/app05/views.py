from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
from app05 import models
from django.core import serializers
import time


# Create your views here.

def demo1(request):
    if request.method == 'POST':
        # print(request.POST)  # ==> <QueryDict: {'i1': ['111'], 'i2': ['222']}>

        # i1 = request.POST.get('i1')
        # i2 = request.POST.get('i2')
        # res = int(i1) + int(i2)
        # return HttpResponse(res)

        """
            1.HttpResponse不能返回字典类型数据,并且返回的数据需要格式化方便前端取值展示
            2.后端如果是用HttpResponse返回数据 回调函数不会自动帮你反序列化, 非要用可以在后端先将数据序列化好在返回
            3.推荐使用JSONResponse返回数据,回调函数可以自动反序列化
        """
        d = {'username': 'jason', 'age': 18}
        return JsonResponse(d)
    return render(request, 'app05/a1.html')


def index(request):
    if request.method == 'POST':
        print(request.POST)  # ==> <QueryDict: {'username': ['Jason'], 'password': ['123']}>
        print(request.FILES)  # ==> <MultiValueDict: {'file': [<InMemoryUploadedFile: 正则.png (image/png)>]}>
    return render(request, 'app05/index.html')


def ab_json(request):
    if request.method == 'POST':
        # print(request.is_ajax())  # ==> True 判断是否是Ajax请求
        # print(request.body)  # ==> b'{"username":"jason","age":18}'
        json_bytes = request.body

        # 针对JSON数据手动处理
        # json_str = json_bytes.decode('utf-8')
        # json_dict = json.loads(json_str)
        # print(json_dict)  # ==> {'username': 'jason', 'age': 18}–

        # json.loads括号内如果传入了一个二进制格式的数据那么内部会自动解码再反序列化
        json_dict = json.loads(json_bytes)  # json_bytes = b'{"username":"jason","age":18}'
        print(json_dict)  # ==> {'username': 'jason', 'age': 18}

    return render(request, 'app05/ab_json.html')


def ab_file(request):
    if request.method == 'POST':
        print(request.POST)  # ==> <QueryDict: {'username': ['Jason'], 'password': ['12345']}>
        print(request.FILES)  # ==> <MultiValueDict: {'myfile': [<InMemoryUploadedFile: logo.jpeg (image/jpeg)>]}>

    return render(request, 'app05/ab_file.html')


def ab_ser(request):
    # 手动
    """
        手动序列化返回数据
        :param request:
        :return: 返回序列化的数据
            [
                 {"id": 1, "username": "jason", "age": 18, "gender": "male"},
                 {"id": 2, "username": "vivi", "age": 18, "gender": "female"},
                 {"id": 3, "username": "tom", "age": 18, "gender": "others"},
                 {"id": 4, "username": "jack", "age": 18, "gender": 4},
                 {"id": 5, "username": "lili", "age": 18, "gender": "female"}
             ]
    """
    # user_queryset = models.User.objects.all()
    # user_list = []
    # for user_obj in user_queryset:
    #     tmp = {
    #         'id': user_obj.pk,
    #         'username': user_obj.username,
    #         'age': user_obj.age,
    #         'gender': user_obj.get_gender_display()
    #     }
    #     user_list.append(tmp)
    # return JsonResponse(user_list, safe=False)

    # 模块化
    """
    自动帮你将数据序列化为JSON格式字符串
        [
            {"model": "app05.user", "pk": 1, "fields": {"username": "jason", "age": 18, "gender": 1}}, 
            {"model": "app05.user", "pk": 2, "fields": {"username": "vivi", "age": 18, "gender": 2}}, 
            {"model": "app05.user", "pk": 3, "fields": {"username": "tom", "age": 18, "gender": 3}}, 
            {"model": "app05.user", "pk": 4, "fields": {"username": "jack", "age": 18, "gender": 4}}, 
            {"model": "app05.user", "pk": 5, "fields": {"username": "lili", "age": 18, "gender": 2}}
        ]
    """
    user_queryset = models.User.objects.all()
    res = serializers.serialize('json', user_queryset)
    return HttpResponse(res)


def user_list(request):
    user_queryset = models.User.objects.all()

    return render(request, 'app05/user_list.html', locals())


def user_delete(request):
    if request.is_ajax():
        if request.method == 'POST':
            back_dic = {"code": 10001, "msg": ""}
            time.sleep(5)
            delete_id = request.POST.get('delete_id')
            models.User.objects.filter(pk=delete_id).delete()
            back_dic['msg'] = '数据删除成功'
            return JsonResponse(back_dic)


def ab_bulk_insert(request):
    book_list = []
    for i in range(1000):
        book_obj = models.Book(title='第%s本书' % i)
        book_list.append(book_obj)
    models.Book.objects.bulk_create(book_list)
    book_queryset = models.Book.objects.all()

    return render(request, 'app05/ab_bulk_insert.html', locals())


def ab_paging(request):
    """
        分页首先需要知道有多少页, 每页展示多少条,首条和尾条是什么, 首页和尾页, 展示第几页, 共计需要展示多少页



        per_page_num=10
        current_page  start_page  end_page
            1           0           10
            2           10          20
            3           20          30
            x          10*(x-1)     10x
    """
    book_list = models.Book.objects.all()

    # 每页展示多少条
    per_page_num = 10

    # 获取到用户想要访问的数据页码
    current_page = request.GET.get('page', 1)
    try:
        current_page = int(current_page)
    except Exception:
        current_page = 1

    # 计算每页的收尾数据
    start_page = per_page_num * (current_page - 1)
    end_page = per_page_num * current_page

    # 计算有多少页码
    book_count = book_list.count()
    page_count, more = divmod(book_count, per_page_num)
    if more:
        page_count += 1

    # 用来避免页码选择器保证不出现负数
    button_page = current_page
    if button_page < 6:
        current_page = 6

    # 生成HTML代码往前端塞
    page_html = ''
    for i in range(current_page - 5, current_page + 6):
        if button_page == i:
            page_html += '<li class="active"><a href="?page=%s">%s</a></li>' % (i, i)
        else:
            page_html += '<li><a href="?page=%s">%s</a></li>' % (i, i)

    # 返回切片的数据
    book_queryset = book_list[start_page:end_page]
    return render(request, 'app05/ab_paging.html', locals())


def my_paging(request):
    from utils.mypage import Pagination
    # 获取到当前页码
    current_page = request.GET.get('page', 1)
    # 获取所有数据对象
    book_queryset = models.Book.objects.all()
    # 统计书籍总数
    all_count = book_queryset.count()
    # 调用第三方分页插件生成对象
    page_obj = Pagination(current_page=current_page, all_count=all_count)
    # 分页返回数据
    page_queryset = book_queryset[page_obj.start:page_obj.end]
    return render(request, 'app05/my_paging.html', locals())


'form组件相关'


def f_form(request):
    """
        实现一个注册功能,获取用户名密码,利用form表单提交数据,后端判断条件,并返回错误
    """
    back_dic = {"username_err": "", "password_err": ""}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username)

        if 'tom' in username.lower():
            back_dic["username_err"] = "不允许Tom注册"
        if len(password) < 8:
            back_dic["password_err"] = "密码不能小于8位"

    return render(request, 'app05/f_form.html', locals())


#
from django import forms
from django.core.validators import RegexValidator  # 自定义验证


class MyForm(forms.Form):
    """
        label 别名, error_messages 自定义报错信息,  initial 默认值,
        required  控制字段是否必填 required = False 为不必填
    """
    username = forms.CharField(label="用户名", min_length=3, max_length=8, initial='Jason',
                               error_messages={
                                   'min_length': '用户名最少三位',
                                   'max_length': '用户名最大8位',
                                   'required': '用户名不能为空'},
                               widget=forms.TextInput(attrs={'class': 'form-control c1 c2', 'username': 'jason'})
                               )
    password = forms.CharField(min_length=3, max_length=8, label="密码",
                               error_messages={
                                   'min_length': '密码最少三位',
                                   'max_length': '密码最大8位',
                                   'required': '密码不能为空'},
                               widget=forms.PasswordInput(attrs={'class': 'form-control'})
                               )
    confirm_password = forms.CharField(min_length=3, max_length=8, label="确认密码",
                                       error_messages={
                                           'min_length': '密码最少三位',
                                           'max_length': '密码最大8位',
                                           'required': '密码不能为空'},
                                       widget=forms.PasswordInput(attrs={'class': 'form-control'})
                                       )
    email = forms.EmailField(label="邮箱", error_messages={'invalid': '邮箱格式不正确', 'required': '邮箱不能为空'},
                             widget=forms.EmailInput(attrs={'class': 'form-control'})
                             )
    # 正则校验
    phone = forms.CharField(label='手机号',
                            validators=[
                                RegexValidator(r'^[0-9]+$', '请输入数字'),
                                RegexValidator(r'^159[0-9]+$', '数字必须以159开头'),
                                RegexValidator(r'd{11}', '手机号码必须是十一位')],
                            widget=forms.TextInput(attrs={'class': 'form-control'})
                            )
    #  下拉单选
    gender = forms.ChoiceField(label='性别', choices=((1, 'male'), (2, 'female'), (3, 'secret')),
                               initial=3,
                               widget=forms.Select(attrs={'class': 'form-control'})
                               )

    # 下拉多选
    hobby = forms.MultipleChoiceField(label='爱好', choices=((1, '篮球'), (2, '足球'), (3, '乒乓球')),
                                      initial=[1, 2],
                                      widget=forms.SelectMultiple(attrs={'class': 'form-control'})
                                      )
    # checkbook 单选
    keep = forms.ChoiceField(label='是否记住密码', initial='checked',
                             widget=forms.CheckboxInput()
                             )
    # checkbook 多选
    hobby2 = forms.MultipleChoiceField(label='爱好', choices=((1, '篮球'), (2, '足球'), (3, '乒乓球')),
                                       initial=[1, 2],
                                       widget=forms.CheckboxSelectMultiple()
                                       )

    # 钩子函数
    # 局部钩子
    def clean_username(self):
        """ 校验用户名含有@符号报错 """
        username = self.cleaned_data.get('username')
        if '@' in username:
            self.add_error('username', '用户名不能包含@符号')
        # 将钩子函数勾出来的数据再放回去
        return username

    # 全局钩子
    def clean(self):
        """ 实现密码二次输入校验是否一致 """
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if not password == confirm_password:
            self.add_error('confirm_password', '密码不一致')
        # 将钩子函数勾出来的数据再放回去
        return self.cleaned_data


def f_index(request):
    # 1.先生成一个空对象
    form_obj = MyForm()
    if request.method == "POST":
        """
            获取用户数据并校验
                1.用request.POST.get('username') 方式逐一获取单条数据繁琐
                2.校验数据需要构造成字典格式传入才行
            注意: request.POST 可以看出是一个字典
        """
        # 3.通过MyForm校验request.POST获取到数据
        form_obj = MyForm(request.POST)
        # 4.判断数据是否合法
        if form_obj.is_valid():
            # 5.合法后操作
            return HttpResponse('OK')
        # 5.不合法后续操作

    # 2直接将空对象传递给HTML页面
    return render(request, 'app05/f_index.html', locals())
