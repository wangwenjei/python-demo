from django.test import TestCase

# Create your tests here.
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    import django
    django.setup()

    from blog import models
    # models.UserInfo.objects.create(name='admin', password='admin123.com', email='admin@163.com', is_delete='True')
    # models.UserInfo.objects.create(name='jason', password='jason123.com', email='jason@163.com', is_delete='False')

    user_obj = models.UserInfo.objects.filter(name='admin', is_delete=1)
    if user_obj:
        print(user_obj[0].password)
        pwd = user_obj[0].password
        if pwd == 'admin123.com':
            print('ok')
    else:
        print('err')


if __name__ == '__main__':
    main()
