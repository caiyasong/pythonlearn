from django.db import models

# Create your models here.
class User(models.Model):

    SEX = (
        ('male', '男'),
        ('female', '女')
    )

    phonenum = models.CharField(max_length=20, unique=True, verbose_name="手机号")
    nickname = models.CharField(max_length=40, unique=True, verbose_name="昵称")
    sex = models.CharField(max_length=10, choices=SEX, default='male', verbose_name="性别")
    birth_year = models.IntegerField(default=2001, verbose_name="出生年")
    birth_month = models.IntegerField(default=1, verbose_name="出生月")
    birth_day = models.IntegerField(default=1, verbose_name="出生日")
    avatar = models.CharField(max_length=100, verbose_name="个人形象")
    location = models.CharField(max_length=50, verbose_name="常居地")

    @property
    def profile(self):

        if not hasattr(self, '_profile'):

            self._profile, created = Profile.objects.get_or_create(id=self.id)

        return self._profile

    class Meta:
        db_table = 'sp_user'


    def __str__(self):
        return self.nickname



class Profile(models.Model):
    SEX = (
        ('male', '男'),
        ('female', '女')
    )

    location = models.CharField(max_length=20, verbose_name="目标城市")
    min_distance = models.IntegerField(default=1, verbose_name="最小查找范围")
    max_distance = models.IntegerField(default=20, verbose_name="最大查找范围")
    min_dating_age = models.IntegerField(default=18, verbose_name="最小交友年龄")
    max_dating_age = models.IntegerField(default=50, verbose_name="最大交友年龄")
    dating_sex = models.CharField(max_length=20, choices=SEX, verbose_name="匹配的性别")

    class Meta:
        db_table = 'sp_profile'