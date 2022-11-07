#1.定义中间件
from django.utils.deprecation import MiddlewareMixin
class MyMiddleware(MiddlewareMixin):
    def __init__(self,get_response=None):
        super().__init__(get_response)
        #初始化中间件
        print('init_mymiddleware')
    def process_request(self,request):
        # 没有return或者return None 继续调用其他视图
        # return response 则不会调用其他视图
        request.context = {}
        if 'session_user' in request.session.keys():
            request.context['session_user']=request.session['session_user']

        #print('process_request')
    def process_response(self,request,response):
        #必须=return response
        print('process_response')
        return response
#2.配置中间件
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware'
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'Middleware.MyMiddleware'
# ]