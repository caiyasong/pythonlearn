from django.db import models

class Swiped(models.Model):
    uid = models.IntegerField(verbose_name="用户自身id")
    sid = models.IntegerField(verbose_name="被滑的陌生人id")
    mark = models.CharField(max_length=20, verbose_name="滑动类型")
    time = models.DateTimeField(auto_now_add=True, verbose_name="滑动的时间")

    class Meta:
        db_table = 'sp_swiped'

    @classmethod
    def add_swiped(cls, uid, sid, mark):
        obj = cls.objects.create(
            uid=uid,
            sid=sid,
            mark=mark
        )

        return obj

    @classmethod
    def get_friend(cls, sid, uid):
        if cls.objects.filter(uid=sid, sid=uid, mark__in=['like', 'superlike']).exists():
            # uid, sid = (uid, sid) if uid < sid else (sid, uid)
            uid1 = max(uid, sid)
            uid2 = min(uid, sid)
            Friend.objects.get_or_create(
                uid1=uid1,
                uid2=uid2
            )

class Friend(models.Model):
    uid1 = models.CharField(verbose_name='uid1')
    uid2 = models.CharField(verbose_name='uid2')

    class Meta:
        db_table = 'sp_friend'