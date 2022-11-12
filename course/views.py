from django.shortcuts import render
from .models import Course,Category
# Create your views here.
def index_handler(request):
    context = request.context
    category_s =Category.objects.all()
    course_data_s = []
    for category in category_s:
        course_data_s.append(
            {
                'category':category.name,
                'course_s':category.courses_set.all()
            }
        )
    context['course_data_s']=course_data_s

    return render(request,'index.html',context)


def course_handler(request,course_id):

    
    return render(request,'course.html')


def video_handler(request,course_id):
    return None


def videoStream_handler(request,course_id):
    return None