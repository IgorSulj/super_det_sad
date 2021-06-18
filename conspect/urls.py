from django.urls import path
from django.views.generic import TemplateView, DetailView, CreateView

from .models import SubjectModel, StructureComponentModel, AnswerModel
from .views import LessonView, lessons, SubjectView, MyCreateView

app_name = 'conspect'


urlpatterns = [
    # path('', LessonView.as_view(), name='lessons'),
    path('', TemplateView.as_view(template_name='home_page.html'), name='home'),
    path('conspect/', lessons, name='lessons_tmp'),
    path('conspect/<int:pk>', SubjectView.as_view(), name='lesson'),
    path('add_subject/', MyCreateView.as_view(model=SubjectModel), name='add_subject'),
    path('add_component/', MyCreateView.as_view(model=StructureComponentModel), name='add_component'),
    path('add_answer/', MyCreateView.as_view(model=AnswerModel), name='add_answer'),
]
