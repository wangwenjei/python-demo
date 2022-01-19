from django.shortcuts import HttpResponse, render
from django.views import View
from app06 import notify


class Notify(View):
    def get(self, request):
        return render(request, 'app06/notify.html')

    def post(self, request):
        notify_content = request.POST.get('notify_content')
        notify.sed_all(notify_content)

        return HttpResponse('is ok')
