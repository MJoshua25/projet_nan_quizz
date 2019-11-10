from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Q
from datetime import datetime
import pytz
from . import models
# Create your views here.

def dashboard(request):
    return render(request, 'pages/dashboard/dashboard.html' )

def resultat(request):
    return render(request, 'pages/dashboard/resultat.html' )
    
def home(request):
    now = datetime.now()
    now = pytz.utc.localize(now)
    q = models.Quizz.objects.filter(statut=True).filter(specialisation__nom = request.user.profile.specialisation.nom)
    al = [i.quizz.id for i in request.user.quizzs.all()]
    att = q.exclude(id__in=al)
    q_att = [a for a in att if a.is_available]
    id_v = [i.id for i in q_att]
    p = q.exclude(id__in=id_v)
    # p = q.filter((Q(date_debut__gte = now)&Q(id__in=al)), Q(date_fin__gte = now))

    data={
        'q_att': q_att,
        'q_pass': p
    }
    return render(request, 'pages/index.html',data)

def quizz(request):
    data={}
    return render(request, 'pages/quizz.html',data)

def result(request):
    data={}
    return render(request, 'pages/result.html',data)


def register(request):
    return render(request, "pages/comptes/register.html")

def connexionuser(request):
    return render(request, "pages/comptes/login.html")