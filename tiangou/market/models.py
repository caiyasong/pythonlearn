from django.db import models

# Create your models here.
class Goods(models.Model):
    productid = models.CharField(max_length=100, verbose_name="商品编号")
    productimg = models.CharField(max_length=100, verbose_name="商品图片")
    content = models.CharField(max_length=1000, verbose_name="商品内容")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="商城价格")
    marketprice = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="价格")
    storenums = models.IntegerField(verbose_name="库存")
    productnum = models.IntegerField(verbose_name="销量")

    class Meta:
        db_table = 'tg_goods'