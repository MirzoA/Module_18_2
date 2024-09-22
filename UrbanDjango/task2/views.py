from django.shortcuts import render
from django.views.generic import TemplateView

class ClassViewTemplate(TemplateView):
    template_name = 'second_task/class_template.html'

def function_view(request):
    return render(request, 'second_task/func_template.html')
    
# Create your views here.
