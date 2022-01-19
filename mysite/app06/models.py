from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

"""
报错
auth.User.user_permissions: (fields.E304) Reverse accessor for 'auth.User.user_permissions' clashes with reverse accessor for 'app06.UserInfo.user_permissions'.
        HINT: Add or change a related_name argument to the definition for 'auth.User.user_permissions' or 'app06.UserInfo.user_permissions'.

"""


class UserInfo(AbstractUser):
    phone = models.BigIntegerField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
