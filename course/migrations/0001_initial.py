# Generated by Django 3.1.1 on 2022-10-13 03:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='课程种类')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=40, verbose_name='课程名称')),
                ('fileName', models.FileField(upload_to='', verbose_name='文件名称')),
                ('imgName', models.ImageField(upload_to='', verbose_name='课程图片')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='售价')),
                ('summary', models.CharField(default='', max_length=1000, verbose_name='课程介绍')),
                ('status', models.PositiveIntegerField(default=0, verbose_name='状态')),
                ('createDatetime', models.DateTimeField(default=datetime.datetime(2022, 10, 13, 11, 10, 56, 276955), verbose_name='创建时间')),
                ('pCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses_set', to='course.category', verbose_name='课程类别')),
                ('userBuyer', models.ManyToManyField(related_name='userBuyer_set', to='user.User', verbose_name='购买用户')),
                ('userShoppingcart', models.ManyToManyField(related_name='userShoppingcart_set', to='user.User', verbose_name='加入购物车的用户')),
            ],
        ),
    ]
