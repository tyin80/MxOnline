from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER_CHOICE = (
    ('male', '男'),
    ('female', '男'),
)


class BaseModel(models.Model):
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        # 设置abstract使BaseModel不会生成表
        abstract = True


# UserProfile继承auth_user表并且覆盖它，setting添加AUTH_USER_MODEL
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name="昵称", default="")
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    gender = models.CharField(verbose_name="性别",choices=GENDER_CHOICE, max_length=6)
    address = models.CharField(verbose_name="地址", max_length=100, default="")
    mobile = models.CharField(verbose_name="手机号", max_length=11)
    images = models.ImageField(verbose_name="头像", upload_to="head_image/%Y/%M", default="default.jpg")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.nick_name:
            return self.nick_name
        else:
            return self.username
