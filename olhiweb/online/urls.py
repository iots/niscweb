from django.conf.urls import  url,patterns

urlpatterns = patterns("",
    url(r'^online/$','online.views.online',name='online'),
)