from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Q
from datetime import datetime
import pytz
from . import models
# Create your views here.

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.http import JsonResponse
import json


def dashboard(request):
    return render(request, 'pages/dashboard/dashboard.html' )


def resultat(request):
    return render(request, 'pages/dashboard/resultat.html' )

@login_required(login_url='connexionuser')
def home(request):
    now = datetime.now()
    now = pytz.utc.localize(now)
    q = models.Quizz.objects.filter(statut=True).filter(specialisation = request.user.profile.specialisation)
    qt = models.Quizz.objects.filter(statut=False).filter(specialisation__nom = request.user.profile.specialisation)
    b = q.count()
    print(b,'2222222')
    print(q,'++++++++++++++++++++++++11111111')
    #print(q[0].titre)
    print(qt.count())
    # num = q.count()
    # i = 0
    # bb = [a for a in q if i < num ]
    # print(bb[1], '000000000000000000111111111')
    # while i < num :
    #     qq = models.Quizz.objects.filter(statut=True).filter(specialisation__nom = request.user.profile.specialisation)
    #     i += 1
    #     qqq = i-1
    #     print(qqq, '00000000000000000011111122221')
        #q[1].titre
    
    
    # al = [i.quizz.id for i in request.user.quizzs.all()]
    # print('======',al)
    # att = q.exclude(id__in=al)
    # print('====',att)
    # q_att = [a for a in att if a.is_available]
    # print('+++++++++++++',q_att)
    # id_v = [i.id for i in q_att]
    # print('id_v', id_v)
    # p = q.exclude(id__in=id_v)
    # p = q.filter((Q(date_debut__gte = now)&Q(id__in=al)), Q(date_fin__gte = now))
    # print('------ p', p)

    data={
        # 'q_att': q_att,
        'q': q,
        'qt': qt,
        # 'num': num,
        'b':b,
        # 'qq': qq,
        # 'qqq': qqq,
    }
    return render(request, 'pages/index.html',data)

def quizz(request):
    data={}
    return render(request, 'pages/quizz.html',data)

@login_required(login_url='connexionuser')
def result(request):
    data={}
    return render(request, 'pages/result.html',data)


def register(request):
    specialite = models.Specialisation.objects.filter(statut=True)

    data = {
        'specialite': specialite,
    }
    return render(request, "pages/comptes/register.html", data)

def connexionuser(request):
    return render(request, "pages/comptes/login.html")

def registerApi(request):
      
    firstname = request.POST.get('first_name')
    lastname = request.POST.get('last_name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    # image = request.FILES['file']
    image = request.FILES.get('file')
    print('vvgsgsgsggs', firstname)
    print('vvgsgsgsggs', username)
    print('vvgsgsgsggs', image)
    is_email=False       
    Min_Length = 8
    

    if firstname != '' and lastname != '' and username != '' and email != '' and image != '' :

        try:
            validate_email(email)
            is_email=True
        except:
            data = {
                'success' : False,
                'message' : 'Email is not valide'
            }

        if is_email :

            try :

                user_dup = User.objects.filter(email=email)
                user_dupli = User.objects.filter(username=username)
                
                if user_dup.exists():
                    
                    data={
                        'success':False,
                        'message': 'Ce mail existe Deja dans la BD'
                    }

                elif user_dupli.exists():

                    data = {
                        'success' : False,
                        'message': 'Votre Username existe deja'
                    }

                elif len(password) < Min_Length:
                    data = {
                        'success':False,
                        'message': 'Mot de passe doit etre au minimum 8 chiffres'
                    }

                elif password == password2 and (password != '' and password2 != ''):
                    user = User(username = username, first_name = firstname, last_name = lastname, email = email)
                    user.save()
                    user.profile.image = image
                    user.save()
                    user.password = password
                    user.set_password(user.password)
                    user.save()

                    data={
                        'success':True,
                        'message': 'Enregistrement effectue avec succes'
                    }

                else:
                    data={
                        'success':False,
                        'message':'Mot de passe ne sont pas meme'
                    }

            except:
                pass
    
    else :
        data = {
            'success' : False,
            'message':'Verifier les Champs'
        }

    return JsonResponse(data, safe=False)


def loginsApi(request):

    postdata = json.loads(request.body.decode('utf-8'))
    username = postdata['username']
    password = postdata['password']
    print("###################user", username) 
    print("###################user", password) 
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        print("###################user is login")   
        login(request, user)

        data={
            'success':True,
            'message':'connecte'
        }

    else:

        data={
            'success':False,
            'message':'Erro Login...'
        }
    return JsonResponse(data, safe=False)


def logout_view(request):
    logout(request)
    return redirect('connexionuser')
