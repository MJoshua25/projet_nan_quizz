from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('quizz/', views.quizz, name='quizz'),
    path('result', views.result, name='result'),
]