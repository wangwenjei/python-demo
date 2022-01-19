from django.shortcuts import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class MyMiddleware1(MiddlewareMixin):
    def process_request(self, request):
        print('我是第 一 个自定义中间件里面的process_request方法')
        # return HttpResponse('is ok')  # 请求将在此处掉头返回

    def process_response(self, request, response):
        print('我是第 一 个自定义中间件里面的process_response方法')
        return response  # 没有返回值则报错 'NoneType' object has no attribute 'get'

    def process_view(self, request, view_name, *args, **kwargs):
        # print(view_name, args, kwargs)  # ==> <function index at 0x105ad34c0> ((), {}) {}
        print('我是第 一 个自定义中间件里面的process_view')

    def process_template_response(self, request, response):
        print('我是第 一 个自定义中间件里面的process_template_response')
        return response

    def process_exception(self,request,exception):
        print('我是第 一 个中间件里面的process_exception')
        print(exception)

class MyMiddleware2(MiddlewareMixin):
    def process_request(self, request):
        print('我是第 二 个自定义中间件里面的process_request方法')

    def process_response(self, request, response):
        print('我是第 二 个自定义中间件里面的process_response方法')
        return response

    def process_view(self, request, view_name, *args, **kwargs):
        # print(view_name, args, kwargs)
        print('我是第 二 个自定义中间件里面的process_view')

    def process_template_response(self, request, response):
        print('我是第 一 个自定义中间件里面的process_template_response')
        return response

    def process_exception(self,request,exception):
        print('我是第 二 个中间件里面的process_exception')
        print(exception)