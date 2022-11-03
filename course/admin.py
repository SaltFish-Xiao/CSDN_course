from django.contrib import admin
from .models import Category,Course
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    #填写外键
    filter_horizontal = ['userBuyer','userShoppingcart']
    #展示的字段
    list_display = ['id','pCategory','courseName','price','status','createDatetime']
    #过滤器字段
    list_filter = ['status','createDatetime']
    #模糊查询字段
    search_fields = ['courseName','price']