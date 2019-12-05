from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Create your models here.

#用户表
class UserAdmin(models.Model):
    class Meta:
        verbose_name = "用户"
        verbose_name_plural ="用户"
    username = models.CharField(max_length=20,verbose_name='用户名')
    password = models.CharField(max_length=20,verbose_name='密码')

#电影信息表
class MovieInformation(models.Model):
    class Meta:
        verbose_name = "电影信息"
        verbose_name_plural ="电影信息"
    mname = models.CharField(max_length=200,verbose_name='电影名称')
    years = models.CharField(max_length=20,verbose_name='年份')
    score = models.CharField(max_length=20,verbose_name='评分')
    director = models.CharField(max_length=1000,verbose_name='导演')
    mold = models.CharField(max_length=200,verbose_name='类型')
    act = models.CharField(max_length=1000,verbose_name='演员')
    languages = models.CharField(max_length=200,verbose_name='语言')
    img = models.CharField(max_length=200,verbose_name='电影图片地址')
    details = models.CharField(max_length=200,verbose_name='电影详情')
    official = models.CharField(max_length=200,verbose_name='电影官方网址')
    def __str__(self):
        return self.mname

#TOP
class MovieTop(models.Model):
    class Meta:
        verbose_name = "电影排行"
        verbose_name_plural ="电影排行"
    mname = models.CharField(max_length=200,verbose_name='电影名称')
    years = models.CharField(max_length=20,verbose_name='年份')
    score = models.CharField(max_length=20,verbose_name='评分')
    director = models.CharField(max_length=1000,verbose_name='导演')
    mold = models.CharField(max_length=200,verbose_name='类型')
    act = models.CharField(max_length=1000,verbose_name='演员')
    img = models.CharField(max_length=200,verbose_name='电影图片地址')
    details = models.CharField(max_length=200,verbose_name='电影详情')

#收藏表
class MovieCollection(models.Model):
    class Meta:
        verbose_name = "电影收藏"
        verbose_name_plural = "电影收藏"
    uid = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户ID')
    mid = models.ForeignKey(MovieInformation,on_delete=models.CASCADE,verbose_name='电影名称')



from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
