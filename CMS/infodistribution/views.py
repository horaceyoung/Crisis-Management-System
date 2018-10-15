from django.shortcuts import render


def department_home(request):
    return render(request, 'department/department_home.html')
