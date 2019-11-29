from django.db import models

class Vip(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name="vip分类名称")
    level = models.IntegerField(verbose_name="等级")
    price = models.FloatField(verbose_name="价格")

    # vip 对应的权限
    @property
    def all_perm(self):
        objs = VipPermRelation.objects.filter(vip_id=self.id)
        #[<VipPermRelation>, <VipPermRelation>, <VipPermRelation>]
        #[perm_id1, perm_id2, perm_id3]
        perm_idlist = [obj.perm_id for obj in objs]
        return Permission.objects.filter(id__in=perm_idlist)

    def __str__(self):
        return self.name


    class Meta:
        db_table = 'sp_vip'


class Permission(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="权限名称")
    description = models.CharField(max_length=250, verbose_name="权限说明")

    class Meta:
        db_table = 'sp_permission'

    def __str__(self):
        return self.name


class VipPermRelation(models.Model):
    vip_id = models.IntegerField(verbose_name="vipid")
    perm_id = models.IntegerField(verbose_name="权限id")

    class Meta:
        db_table = 'sp_vip_perm_relation'