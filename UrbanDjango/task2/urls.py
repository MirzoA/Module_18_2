from django.urls import path
from .views import ClassViewTemplate, function_view

urlpatterns = [
    path('class-view/', ClassViewTemplate.as_view(), name='class_view'),
    path('function-view/', function_view, name='function_view'),
]
