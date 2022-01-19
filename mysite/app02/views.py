from django.shortcuts import render, HttpResponse, redirect
from django.views import View  #


# Create your views here.

def roule001(request):
    return HttpResponse('this is app02 roule001')


class MyLogin(View):
    def get(self, request):
        return render(request, 'app02/form.html')

    def post(self, request):
        return HttpResponse('post方法')


# 上传文件
class UploadFile(View):
    def get(self, request):
        return render(request, 'app02/upload_file.html')

    def post(self, request):
        # print(request.FILES)  # <MultiValueDict: {'UploadFile': [<InMemoryUploadedFile: 正则.png (image/png)>]}>
        file_obj = request.FILES.get('UploadFile')
        file_name = file_obj.name
        with open(r'static/file/' + file_name, 'wb') as f:
            for line in file_obj.chunks():  # 推荐加上chunks方法 其实跟不加是一样的都是一行行的读取
                f.write(line)

        return HttpResponse('file upload is ok')
