from django.db import models

# Create your models here.


class Orders(models.Model):
    uid = models.IntegerField(verbose_name='用户id')
    gid = models.CharField(max_length=80, verbose_name='商品id')
    gnum = models.IntegerField(verbose_name='商品数量')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="商品价格")
    totalprice = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="商品总价格")

    class Meta:
        db_table = "tg_order"