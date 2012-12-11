#from account.forms import ResetPasswordForm, SetPasswordForm, SignupForm
from django.http import HttpResponse,HttpResponseRedirect
from account.models import Account
#from patient_management import models as patientmgm
from newsfeed.models import Status
from newsfeed.forms import StatusForm
from patient_management.models import Patientdetail
from django.views.generic.simple import direct_to_template
from django.shortcuts import redirect, render
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User

from django.utils import simplejson

import glob
import os

def group_and_bridge(kwargs):
    """
    Given kwargs from the view (with view specific keys popped) pull out the
    bridge and fetch group from database.
    """
    
    bridge = kwargs.pop("bridge", None)
    
    if bridge:
        try:
            group = bridge.get_group(**kwargs)
        except ObjectDoesNotExist:
            raise Http404
    else:
        group = None
    
    return group, bridge


def group_context(group, bridge):
    # @@@ use bridge
    return {
        "group": group,
    }

def return_icons(request, **kwargs):
    os.chdir("/home/quanke/elderlove-v4/static/img/mood-icon/negative")
    icondir = {}
    neglist = []
    for files in glob.glob("*.png"):
        neglist.append(str(files))
    icondir["negative"] = neglist
    os.chdir("/home/quanke/elderlove-v4/static/img/mood-icon/positive")
    poslist = []
    for files in glob.glob("*.png"):
        poslist.append(str(files))
    icondir["positive"] = poslist
    os.chdir("/home/quanke/elderlove-v4/static/img/mood-icon/neutral")
    neulist = []
    for files in glob.glob("*.png"):
        neulist.append(str(files))
    icondir["neutral"] = neulist
    os.chdir("/home/quanke/elderlove-v4")
    return render(request, 'newsfeed/mainpage.html', icondir)


def post_status(request, **kwargs):
    account  = Account.objects.get(user=request.user)
    accounttype = account.accounttype
    user = account.user

    group, bridge = group_and_bridge(kwargs)

    try:
        message = request.POST['message']
        if account.accounttype == "patient":
            patient = Patientdetail.objects.get(user=user)
            patient.sociability = patient.sociability + 1
            patient.save()
            status = Status(user = user, message = message)
            status.save()
        # update patient's score

        return HttpResponseRedirect('/')
    except KeyError:
        # Redisplay the poll voting form.
        #return render(request, 'patient_management/all_patients.html', {
         #   'error_message': "You didn't select a choice.",
        #})
        return HttpResponse("no haven't"+request.POST['patient_name'])

def post_mood(request, **kwargs):
    account  = Account.objects.get(user=request.user)
    accounttype = account.accounttype
    user = account.user

    group, bridge = group_and_bridge(kwargs)

    try:
        message = request.POST['message']
        if account.accounttype == "patient":
            patient = Patientdetail.objects.get(user=user)
            patient.sociability = patient.sociability + 1
            patient.save()
            mood = Mood(user = user, message = message)
            mood.save()
        # update patient's score

        return HttpResponseRedirect('/')
    except KeyError:
        # Redisplay the poll voting form.
        #return render(request, 'patient_management/all_patients.html', {
         #   'error_message': "You didn't select a choice.",
        #})
        return HttpResponse("no haven't"+request.POST['patient_name'])