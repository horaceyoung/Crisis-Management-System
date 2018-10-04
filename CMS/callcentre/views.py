from django.shortcuts import render


def callcentre_home(request):
    return render(request, 'callcentre/callcentre_home.html')
