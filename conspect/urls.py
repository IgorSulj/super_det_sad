from django.urls import path
from django.views.generic import TemplateView, DetailView

from .models import SubjectModel
from .views import LessonView, lessons, SubjectView

app_name = 'conspect'


urlpatterns = [
    # path('', LessonView.as_view(), name='lessons'),
    path('', TemplateView.as_view(template_name='home_page.html'), name='home'),
    path('conspect/', lessons, name='lessons_tmp'),
    path('conspect/<int:pk>', SubjectView.as_view(), name='lesson'),

]