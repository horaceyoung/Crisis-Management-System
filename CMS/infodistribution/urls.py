from django.urls import path
from . import views

app_name = 'department'

urlpatterns = [
    path('', views.department_home, name='department_home'),
]