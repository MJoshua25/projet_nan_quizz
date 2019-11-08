from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date

class Timemodels(models.Model):
    statut = models.BooleanField(default=False)
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)
      
    class Meta:
        abstract = True

# Create your models here.
class Specialisation(Timemodels):
    """Model definition for Specialisation."""

    # TODO: Define fields here
    nom = models.CharField(max_length=50)
    langage = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Specialisation."""

        verbose_name = 'Specialisation'
        verbose_name_plural = 'Specialisations'

    def __str__(self):
        """Unicode representation of Specialisation."""
        return self.nom


class Profile(models.Model):
    """Model definition for UserProfile."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    specialisation = models.ForeignKey('Specialisation', related_name='users', on_delete=models.CASCADE)

    class Meta:
        """Meta definition for UserProfile."""

        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'

    def __str__(self):
        """Unicode representation of UserProfile."""
        return self.user.username


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, created, **kwargs):
        instance.profile.save()

class Quizz(Timemodels):
    """Model definition for Quizz."""

    # TODO: Define fields here
    specialisation = models.ForeignKey('Specialisation', related_name='quizzs', on_delete=models.CASCADE)
    titre = models.CharField(max_length=50)
    niveau = models.PositiveIntegerField()
    qpv = models.PositiveIntegerField()
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    duree = models.TimeField()

    class Meta:
        """Meta definition for Quizz."""

        verbose_name = 'Quizz'
        verbose_name_plural = 'Quizzs'

    def __str__(self):
        """Unicode representation of Quizz."""
        return "{}: {}".format(self.specialisation, self.titre)

class Question(Timemodels):
    """Model definition for Question."""

    # TODO: Define fields here
    quizz = models.ForeignKey('Quizz', related_name='questions', on_delete=models.CASCADE)
    titre = models.CharField(max_length=50)
    niveau = models.PositiveIntegerField()
    image = models.ImageField(upload_to="question", blank=True, null=True)

    class Meta:
        """Meta definition for Question."""

        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        """Unicode representation of Question."""
        return self.titre

class Reponse(Timemodels):
    """Model definition for Reponse."""

    # TODO: Define fields here
    question = models.ForeignKey('Question', related_name='reponses', on_delete=models.CASCADE)
    titre = models.CharField(max_length=50)
    image = models.ImageField(upload_to="reponse", blank=True, null=True)
    isrtue = models.BooleanField()

    class Meta:
        """Meta definition for Reponse."""

        verbose_name = 'Reponse'
        verbose_name_plural = 'Reponses'

    def __str__(self):
        """Unicode representation of Reponse."""
        return self.titre

class QuizzUser(Timemodels):
    """Model definition for QuizzUser."""

    # TODO: Define fields here
    quizz = models.ForeignKey('Quizz', related_name='quizzuser', on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="quizzs")
    note = models.PositiveIntegerField()

    class Meta:
        """Meta definition for QuizzUser."""

        verbose_name = 'QuizzUser'
        verbose_name_plural = 'QuizzUsers'

    def __str__(self):
        """Unicode representation of QuizzUser."""
        return note


class ReponseUser(Timemodels):
    """Model definition for ReponseUser."""

    # TODO: Define fields here
    question = models.ForeignKey('Question', related_name='reponseuser', on_delete=models.CASCADE)
    quizzuser = models.ForeignKey('QuizzUser', related_name='questions', on_delete=models.CASCADE)
    reponses = models.ManyToManyField('Reponse')
    istrue = models.BooleanField()

    class Meta:
        """Meta definition for ReponseUser."""

        verbose_name = 'ReponseUser'
        verbose_name_plural = 'ReponseUsers'

    def __str__(self):
        """Unicode representation of ReponseUser."""
        return self.istrue




