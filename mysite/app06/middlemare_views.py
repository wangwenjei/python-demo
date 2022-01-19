from django.shortcuts import HttpResponse, render
from django.views.decorators.csrf import csrf_protect, csrf_exempt  # CSRF装饰器
from django.utils.decorators import method_decorator  # CBV装饰器
from django.views import View


def index(request):
    # print('=== index ===')
    # return HttpResponse('index')

    print('我是视图函数index')
    obj = HttpResponse('index')

    # aaaaa

    def render():
        print('内部的render')
        return HttpResponse("O98K")

    obj.render = render
    return obj


# @csrf_protect  # 需要校验
# @csrf_exempt   # 不需要校验
def csrf(request):
    if request.method == 'POST':
        username = request.POST.get('userName')
        target = request.POST.get('targetName')
        money = request.POST.get('money')

        print('%s 给 %s 转账了 %s$' % (username, target, money))

    return render(request, 'app06/csrf.html')


# @method_decorator(csrf_protect, name='post')     # 可以实现
# @method_decorator(csrf_exempt, name='post')      # 不可以实现
# @method_decorator(csrf_exempt, name='dispatch')  # 可以实现,等价于在dispatch上添加装饰器
class MyCsrf(View):
    # @method_decorator(csrf_protect)  # 可以实现
    # @method_decorator(csrf_exempt)   # 可以实现
    def dispatch(self, request, *args, **kwargs):
        return super(MyCsrf, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'app06/csrf.html')

    # @method_decorator(csrf_protect)  # 可以实现
    # @method_decorator(csrf_exempt)   # 不可以实现
    def post(self, request):
        username = request.POST.get('userName')
        target = request.POST.get('targetName')
        money = request.POST.get('money')

        print('%s 给 %s 转账了 %s$' % (username, target, money))
        return HttpResponse('is ok')
