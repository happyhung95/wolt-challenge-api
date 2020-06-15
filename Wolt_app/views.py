from django.shortcuts import render


def home(request):
    return render(request,'Wolt_app/home.html')
