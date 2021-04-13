from django.urls import path
from .views import index, jobs 

urlpatterns= [
    path('', index, name='index'),
    path('home/', jobs, name='jobs'),
]