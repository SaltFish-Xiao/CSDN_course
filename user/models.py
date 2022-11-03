from django.db import models

# Create your models here.
class User(models.Model):
    #将在页面中展示的表面替换成中文
    class Meta():
        verbose_name = verbose_name_plural = '用户表'
    account = models.CharField(max_length=16,unique=True,verbose_name='账号')
    password = models.CharField(max_length=16,verbose_name='密码')
    username = models.CharField(max_length=16,verbose_name='用户名',blank=True)
    money = models.DecimalField(max_digits=12,decimal_places=2,default=0,verbose_name='余额')
    gender = models.PositiveIntegerField(default=0,verbose_name='性别',choices=((0,'男'),(1,'女')))
    # blank=True 表示可为空
    tel = models.CharField(max_length=11,default='',verbose_name = '手机号',blank=True)
    def __str__(self):
        return self.account
