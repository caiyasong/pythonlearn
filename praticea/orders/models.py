from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100, unique=True, verbose_name="用户名")
    password = models.CharField(max_length=200, verbose_name="密码")
    phone = models.CharField(max_length=20, verbose_name="手机号")
    email = models.CharField(default='', max_length=50, verbose_name="邮箱")
    avatar = models.ImageField(upload_to='uploads', verbose_name="头像")
    is_active = models.BooleanField(default=0, verbose_name="激活状态")

    class Meta:
        db_table = 'axf_user'

class Order(models.Model):
    uid = models.IntegerField(verbose_name="用户id")
    order_code = models.CharField(max_length=100, verbose_name="订单编号")
    total_count = models.IntegerField(verbose_name="订单总数量")
    total_amount = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="订单总金额")
    status = models.SmallIntegerField(verbose_name="1未支付，2未发货，3未收货")

    class Meta:
        db_table = 'axf_order'

class OrderDetail(models.Model):
    uid = models.IntegerField(verbose_name="用户id")
    order_code = models.CharField(max_length=100, verbose_name="订单编号")
    goods_id = models.IntegerField(verbose_name="商品id")
    counts = models.IntegerField(verbose_name="商品数量")
    price = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="商品单价")

    class Meta:
        db_table = 'axf_order_detail'