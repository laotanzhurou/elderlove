from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template



urlpatterns = patterns("",
    #url(r"^$", direct_to_template, {"template": "broadcast/familypage.html"}, name="broadcast"),
    url(r"^familypage/$", direct_to_template, {"template": "broadcast/familypage.html"}, name="familypage"),
    url(r"^view_status/$", "broadcast.views.view_patient_status", name="view_status"),
    url(r"^form_kinship/$", "broadcast.views.form_kinship", name="form_kinship"),
    url(r"^find_patient/$", "broadcast.views.show_all_patients", name="find_patient"),
)