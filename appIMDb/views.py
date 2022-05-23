from django.shortcuts import render

def index(request):
    """La home page para la app."""
    return render(request, 'appIMDb/index.html')
