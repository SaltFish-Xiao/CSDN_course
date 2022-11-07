from django.shortcuts import render,HttpResponse
from .models import User
#导入商城首页
from course import views as course_views


# Create your views here.
def index_handler(request):
    return None


def course_handler(request):
    return None


def shoppingCart_handler(request):
    return None


def login_handler(request):
    return None


def register_handler(request):
    if request.method!='POST':
        return  HttpResponse(status=403)
    context = request.context
    account = request.POST.get('account')
    password = request.POST.get('password')
    try:
        user_exists = User.objects.filter(account = account).exists()
        if not user_exists:
            user=User(account=account ,password=password)
            user.save()
            request.session['session_user']={'id':user.id,'account':user.account}
        else:
            context['register_message'] = '账号已存在'

    except:
        context['register_message']='服务器异常'
    finally:
        return course_views.index_handler(request)


def logout_hander(request):
    return None


def puchase_handler(request,course_id):
    return None


def addShoppingCart_handler(request,course_id):
    return None