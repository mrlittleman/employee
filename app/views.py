from django.shortcuts import render

# Create your views here.

def HomeView(request):
    template = 'index.html'
    return render(request, template)