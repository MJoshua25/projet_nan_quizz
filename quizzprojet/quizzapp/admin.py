from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class SpecialisationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'statut',
        'date_add',
        'date_update',
        'nom',
        'langage',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'statut',
        'date_add',
        'date_update',
        'nom',
        'langage',
    )


class ProfileAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'specialisation')
    list_filter = ('user', 'specialisation', 'id', 'user', 'specialisation')


class QuestionInline(admin.TabularInline):
    model =  models.Question
    extra = 0


class QuizzAdmin(admin.ModelAdmin):

    list_display = (
        'statut',
        'date_add',
        'date_update',
        'specialisation',
        'titre',
        'niveau',
        'qpv',
        'date_debut',
        'date_fin',
        'duree',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'specialisation',
        'date_debut',
        'date_fin',
    )

    inlines = [QuestionInline]

class ReponseInline(admin.TabularInline):
    model =  models.Reponse
    extra = 0

class QuestionAdmin(admin.ModelAdmin):

    list_display = (
        'statut',
        'date_add',
        'date_update',
        'quizz',
        'titre',
        'niveau',
        'image',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'quizz',
    )
    inlines = [ReponseInline]


class ReponseAdmin(admin.ModelAdmin):

    list_display = (
        'statut',
        'date_add',
        'date_update',
        'question',
        'titre',
        'image',
        'isrtue',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'question',
        'isrtue',
    )


class QuizzUserAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'statut',
        'date_add',
        'date_update',
        'quizz',
        'user',
        'note',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'quizz',
        'user',
        'id',
        'statut',
        'date_add',
        'date_update',
        'quizz',
        'user',
        'note',
    )


class ReponseUserAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'statut',
        'date_add',
        'date_update',
        'question',
        'quizzuser',
        'istrue',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'question',
        'quizzuser',
        'istrue',
        'id',
        'statut',
        'date_add',
        'date_update',
        'question',
        'quizzuser',
        'istrue',
    )
    raw_id_fields = ('reponses',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Specialisation, SpecialisationAdmin)
_register(models.Profile, ProfileAdmin)
_register(models.Quizz, QuizzAdmin)
_register(models.Question, QuestionAdmin)
_register(models.Reponse, ReponseAdmin)
_register(models.QuizzUser, QuizzUserAdmin)
_register(models.ReponseUser, ReponseUserAdmin)
