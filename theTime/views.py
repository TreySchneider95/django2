from django.shortcuts import render
import datetime

# Create your views here.

def get_time(request):
    context = {}
    context['time'] = datetime.datetime.now()
    return render(request, 'home.html', context)