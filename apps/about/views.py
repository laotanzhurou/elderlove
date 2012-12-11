#from account.forms import ResetPasswordForm, SetPasswordForm, SignupForm
from django.http import HttpResponse,HttpResponseRedirect
from account.models import Account

def what_next(request):
    """
    Given kwargs from the view (with view specific keys popped) pull out the
    bridge and fetch group from database.
    """
    user = request.user
    account  = Account._default_manager.get(user=request.user)
    accounttype = account.accounttype
    if user.is_superuser:
        return HttpResponseRedirect("../../admin")
    elif accounttype=="patient":
    	return HttpResponseRedirect("../../newsfeed")
    elif accounttype=="doctor":
        return HttpResponseRedirect("../../patient_management")
    elif accounttype=="family":
        return HttpResponseRedirect("../../broadcast/familypage")
    else:
        return HttpResponse("accounttype="+accounttype+"lala")
