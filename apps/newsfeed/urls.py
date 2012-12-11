from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template



urlpatterns = patterns("",
    url(r"^$", "newsfeed.views.return_icons",name="newsfeed"),
    url(r"^post_status/$", "newsfeed.views.post_status", name="post_status"),
    #url(r"^return_icons/$", "newsfeed.views.return_icons", name="return_icons"),
)
