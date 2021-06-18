import django.forms
from .models import *
from django.forms import modelform_factory

SubjectForm = modelform_factory(SubjectModel)
StructureComponentForm = modelform_factory(StructureComponentModel)
AnswerForm = modelform_factory(AnswerModel)
