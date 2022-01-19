from django.test import TestCase

# Create your tests here.
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    import django
    django.setup()

    from app05 import models
    models.Book.objects.filter(pk__gt=1000).delete()


if __name__ == '__main__':
    main()
