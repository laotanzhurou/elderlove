from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template


urlpatterns = patterns("",
    url(r"^$", direct_to_template, {"template": "about/about.html"}, name="about"),
    url(r"^terms/$", direct_to_template, {"template": "about/terms.html"}, name="terms"),
    url(r"^test/$", direct_to_template, {"template": "about/test.html"}, name="test"),
    url(r"^privacy/$", direct_to_template, {"template": "about/privacy.html"}, name="privacy"),
    url(r"^dmca/$", direct_to_template, {"template": "about/dmca.html"}, name="dmca"),
    url(r"^what_next/$", "about.views.what_next", name="what_next"),
    url(r"^continues/$", direct_to_template, {"template": "about/what_next.html"}, name="continues"),
)
