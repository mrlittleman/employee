from django.shortcuts import render

# Create your views here.

def HomeView(request):
    template = 'dashboards/home.html'
    return render(request, template)