import datetime
import sys# sys stands for System-specific parameters and functions

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import get_language_from_request, ugettext_lazy as _

from django.contrib.auth.models import User, AnonymousUser
from timezones.fields import TimeZoneField


#class Friendship(models.Model):
    

class Kinship(models.Model):
    patient = models.ForeignKey(User,unique=True,related_name="patient")
    familymember = models.ForeignKey(User,unique=True,related_name="familymember")

   
'''

class Sickness(models.Model):

    sicknessname = models.CharField('disease name',max_length=128,unique=True)

class Takingcare(models.Model):
    
    patientdetail = models.ForeignKey(Patientdetail)
    doctordetail = models.ForeignKey(Doctordetail)

    sickness = models.ForeignKey(Sickness,null = True,blank = True)




    #def __unicode__(self):
     #   return self.user.username
'''
'''
#@receiver(post_save, sender=User)
def create_patient_detail(instance=None):
    if instance is None:
        return
    patientdetail, created = Patientdetail.objects.get_or_create(user=instance)

#@receiver(post_save, sender=User)
def create_doctor_detail(instance=None):
    if instance is None:
        return
    doctordetail, created = Doctordetail.objects.get_or_create(user=instance)


#very very important huh!!!!!!!

#@receiver(post_save, sender=User)

def doctor_takecare_patient(patient, doctor):
    try:
        patientd = Patientdetail.objects.get(user=patient)
        doctord = Doctordetail.objects.get(user=doctor)
        takingcare, created = Takingcare.objects.get_or_create(patientdetail=patientd, doctordetail=doctord)
    except KeyError:
        return False
    return True
'''
