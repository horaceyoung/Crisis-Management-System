from django.shortcuts import render


def department_home(request):
    return render(request, 'infodistribution/department_home.html')
