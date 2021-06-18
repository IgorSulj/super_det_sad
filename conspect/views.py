from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView
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
