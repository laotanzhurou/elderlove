#from account.forms import ResetPasswordForm, SetPasswordForm, SignupForm
from django.http import HttpResponse,HttpResponseRedirect
from account.models import Account
from newsfeed.models import Status
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.views.generic.simple import direct_to_template
from django.shortcuts import redirect, render
from django.utils import simplejson

from patient_management.models import Patientdetail
from broadcast.models import Kinship

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


def show_all_patients(request, **kwargs):
   
    account  = Account.objects.get(user=request.user)
    accounttype = account.accounttype
    user = account.user

    group, bridge = group_and_bridge(kwargs)

    patientlist = []
    for p in Patientdetail.objects.all():
        pd = {}
        pd['username'] = str(p.user.username)
        pd['healthstatus'] = str(p.healthstatus)
        pd['psychostatus'] = str(p.psychostatus)
        pd['sociability'] = str(p.sociability)
        
        patientlist.append(pd)
    
    context = {'patientlist': patientlist}
    return render(request, 'broadcast/add_patient.html', context)

def form_kinship(request, **kwargs):
    account  = Account.objects.get(user=request.user)
    accounttype = account.accounttype
    user = account.user

    if accounttype=='family':
        user2 = User.objects.get(username = request.POST['patient_name'])
        kinship = Kinship(patient=user2, familymember=user)
        kinship.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponse("no haven't"+request.POST['patient_name'])


def view_patient_status(request, **kwargs):
    account  = Account.objects.get(user=request.user)
    accounttype = account.accounttype
    user = account.user

    group, bridge = group_and_bridge(kwargs)

    kinship = Kinship.objects.get(familymember=user)

    user2 = kinship.patient

    statuslist = []
    for s in Status.objects.all():
        if s.user == user2:
            sta = {}
            sta['username'] = str(s.user.username)
            sta['message'] = str(s.message)
            sta['post_time'] = str(s.post_time)       
            statuslist.append(sta)
    
    context = {'statuslist': statuslist}
    return render(request, 'broadcast/view_status.html', context)