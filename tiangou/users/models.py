from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100, verbose_name="用户名", unique=True)
    password = models.CharField(max_length=100, verbose_name="密码")
    email = models.CharField(max_length=100, verbose_name='邮箱')

    class Meta:
        db_table = 'tg_user'