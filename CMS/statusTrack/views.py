from django.shortcuts import render


def statustrack_home(request):
    return render(request, 'statustrack/statustrack_home.html')
