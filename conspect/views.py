from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView
from rest_framework.views import Response, APIView
from .models import *
from .serializers import *



class LessonView(APIView):

    def get(self, request):
        objects = LessonModel.objects.all()
        serializer = LessonSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.POST)
        serializer = LessonSerializer(data=request.data)
        serializer.create_json()
        return HttpResponse(status=201)


@login_required
def lessons(request):

    # subjects = SubjectModel.objects.all()
    structure_components = StructureComponentModel.objects.all()
    subjects = SubjectModel.objects.all()
    context = {'structure_components': structure_components, 'subjects': subjects}
    return render(request, 'index.html', context)


class SubjectView(DetailView):
    queryset = SubjectModel.objects.all()
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super(SubjectView, self).get_context_data(**kwargs)
        context['subjects'] = self.get_queryset()
        return context


class MyCreateView(CreateView):
    template_name = 'creation_form.html'
    fields = '__all__'
    
    def get_success_url(self):
        return f"/{self.request.GET.get('next', None)}" or self.request.path

    def form_valid(self, form):
        super(MyCreateView, self).form_valid(form)
        context = self.get_context_data(message='Создание объекта произошло успешно')
        success_url = self.get_success_url()
        if success_url == self.request.path:
            return self.render_to_response(context)
        else:
            return HttpResponseRedirect(success_url)

