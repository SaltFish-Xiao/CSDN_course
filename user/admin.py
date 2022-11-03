from django.contrib import admin
from .models import User
admin.site.site_header='CSDN微课后台管理'
admin.site.index_title = '后台系统'
admin.site.site_title = '管理'
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    #list_display 定义要显示的字段信息
    list_display = ['id','account','username','money','gender','tel']
    #list_filter 增加过滤器
    list_filter = ['gender','account']
    #search_fields 增加模糊查询
    search_fields = ['account','username']
