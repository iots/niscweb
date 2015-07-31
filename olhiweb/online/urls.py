from django.conf.urls import  url,patterns

urlpatterns = patterns("",
    url(r'^list/$','online.views.online',name='online'),
)