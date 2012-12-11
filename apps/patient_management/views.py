#from account.forms import ResetPasswordForm, SetPasswordForm, SignupForm
from django.http import HttpResponse,HttpResponseRedirect
from account.models import Account
from patient_management import models as patientmgm
from patient_management.models import Patientdetail
from patient_management.models import Doctordetail
from patient_management.models import Takingcare
from django.template import Context, loader
from django.contrib.auth.models import User

from django.views.generic.simple import direct_to_template
from django.shortcuts import redirect, render

from django.utils import simplejson


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


def show_critical_patients(request):
    account  = Account.objects.get(user=request.user)
    accounttype = account.accounttype
    user = account.user

    doctord = Doctordetail.objects.get(user=user)

    patientlist = []
    if len(doctord.patientdetails.all()) != 0:
        #return HttpResponse("You have no patients enroled yet")
        for p in doctord.patientdetails.all:
            '''
            pd = {}
            pd['name'] = str(p.user.username)
            pd['healthstatus'] = str(p.healthstatus)
            pd['psychostatus'] = str(p.psychostatus)
            pd['sociability'] = str(p.sociability)
            '''
            patientlist.append(p)
    return patientlist

def show_my_patients(request, **kwargs):
    account  = Account.objects.get(user=request.user)
    accounttype = account.accounttype
    user = account.user

    group, bridge = group_and_bridge(kwargs)

    doctord = Doctordetail.objects.get(user=user)

    patientlist = []
    for p in doctord.patientdetails.all():
        pd = {}
        pd['username'] = str(p.user.username)
        pd['healthstatus'] = str(p.healthstatus)
        pd['psychostatus'] = str(p.psychostatus)
        pd['sociability'] = str(p.sociability)
    
        patientlist.append(pd)
    context = {'patientlist': patientlist}
    return render(request, 'patient_management/my_patients.html', context)

def show_all_patients(request, **kwargs):
   
    account  = Account.objects.get(user=request.user)
    accounttype = account.accounttype
    user = account.user

    group, bridge = group_and_bridge(kwargs)

    doctord = Doctordetail.objects.get(user=user)
    a = ''
    patientlist = []
    mypatientlist = doctord.patientdetails.all()
    for p in Patientdetail.objects.all():

        if p in mypatientlist:
            a='1'
        else:
            pd = {}
            pd['username'] = str(p.user.username)
            pd['healthstatus'] = str(p.healthstatus)
            pd['psychostatus'] = str(p.psychostatus)
            pd['sociability'] = str(p.sociability)
        
            patientlist.append(pd)
    
    context = {'patientlist': patientlist}
    return render(request, 'patient_management/all_patients.html', context)
    #return HttpResponseRedirect('/patient_management/list_all/')
    #return HttpResponse(simplejson.dumps(patientlist),mimetype="application/json")

def add_patient(request, **kwargs):
    account  = Account.objects.get(user=request.user)
    accounttype = account.accounttype
    user = account.user

    group, bridge = group_and_bridge(kwargs)

    doctord = Doctordetail.objects.get(user=user)

    try:
        user2 = User.objects.get(username = request.POST['patient_name'])
        #selected_patient = Patientdetail.objects.get(user=user2)
        patientmgm.doctor_takecare_patient(user2, user)
        return HttpResponseRedirect('/')
    except (KeyError, User.DoesNotExist):
        # Redisplay the poll voting form.
        #return render(request, 'patient_management/all_patients.html', {
         #   'error_message': "You didn't select a choice.",
        #})
        return HttpResponse("no haven't"+request.POST['patient_name'])


