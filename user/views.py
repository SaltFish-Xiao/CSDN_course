from django.shortcuts import render,HttpResponse,redirect,reverse
from .models import User
#导入商城首页
from course import views as course_views


# Create your views here.
def index_handler(request):
    context = request.context
    session_user = request.session['session_user']
    user = User.objects.get(id = session_user.get('id'))
    context['user']=user
    if request.method == 'GET':
        return render(request,'user.html',context)
    else:
        user.username = request.POST.get('username')
        user.gender = request.POST.get('gender')
        user.tel = request.POST.get('tel')
        user.save()
        return redirect(reverse('user_index'))



def course_handler(request):
    return None


def shoppingCart_handler(request):
    return None


def login_handler(request):
    if request.method !='POST':
        return HttpResponse(status=403)
    context = request.context
    account = request.POST.get('account')
    password = request.POST.get('password')
    user_s = User.objects.filter(account = account,password=password)
    if user_s:
        user = user_s[0]
        request.session['session_user']={'id':user.id,'account':user.account}
        return redirect(reverse('course_index'))
    else:
        context['login_message']='账号或密码错误'
        return course_views.index_handler(request)



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
    request.session['session_user']=None
    return redirect(reverse('course_index'))


def puchase_handler(request,course_id):
    return None


def addShoppingCart_handler(request,course_id):
    return None