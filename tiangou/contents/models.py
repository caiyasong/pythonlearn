from django.db import models

# Create your models here.


# 基类的模型
class Base(models.Model):
    img = models.CharField(max_length=255, verbose_name="图片信息")

    # 这个设置不会让这个模型了映射成数据表
    class Meta:
        abstract = True



# 轮播图模型
class tg_gu(Base):
    # img = models.CharField(max_length=255, verbose_name="图片信息")
    # name = models.CharField(max_length=100, verbose_name="文字信息")

    class Meta:
        db_table = 'tg_gu'


# 导航模型
class tg_hd(Base):
    # img = models.CharField(max_length=255, verbose_name="图片信息")
    # name = models.CharField(max_length=100, verbose_name="文字信息")

    class Meta:
        db_table = 'tg_hd'


# 必买模型
class tg_li(Base):
    # img = models.CharField(max_length=255, verbose_name="图片信息")
    # name = models.CharField(max_length=100, verbose_name="文字信息")

    class Meta:
        db_table = 'tg_li'


# 商店模型
class tg_max(Base):
    # img = models.CharField(max_length=255, verbose_name="图片信息")
    # name = models.CharField(max_length=100, verbose_name="文字信息")

    class Meta:
        db_table = 'tg_max'


class tg_mid(Base):
    # img = models.CharField(max_length=255, verbose_name="图片信息")
    # name = models.CharField(max_length=100, verbose_name="文字信息")

    class Meta:
        db_table = 'tg_mid'


class tg_min(Base):
    # img = models.CharField(max_length=255, verbose_name="图片信息")
    # name = models.CharField(max_length=100, verbose_name="文字信息")

    class Meta:
        db_table = 'tg_min'


class tg_pp(Base):
    # img = models.CharField(max_length=255, verbose_name="图片信息")
    # name = models.CharField(max_length=100, verbose_name="文字信息")

    class Meta:
        db_table = 'tg_pp'


class tg_tg(Base):
    # img = models.CharField(max_length=255, verbose_name="图片信息")
    # name = models.CharField(max_length=100, verbose_name="文字信息")

    class Meta:
        db_table = 'tg_tg'


class tg_zmgd(Base):
    # img = models.CharField(max_length=255, verbose_name="图片信息")
    # name = models.CharField(max_length=100, verbose_name="文字信息")

    class Meta:
        db_table = 'tg_zmgd'