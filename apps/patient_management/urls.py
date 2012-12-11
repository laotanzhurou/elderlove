from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template


urlpatterns = patterns("",
    url(r"^$", direct_to_template, {"template": "patient_management/mainpage.html"}, name="patient_management"),
    url(r"^all_patients/$", "patient_management.views.show_all_patients", name="all_patients"),
    url(r"^critical_patients/$", "patient_management.views.show_critical_patients", name="critical_patients"),
    url(r"^my_patients/$", "patient_management.views.show_my_patients", name="my_patients"),
    url(r"^add_patient/$", "patient_management.views.add_patient", name="add_patient"),
)
