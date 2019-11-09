from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'pages/dashboard/dashboard.html' )

def resultat(request):
    return render(request, 'pages/dashboard/resultat.html' )
