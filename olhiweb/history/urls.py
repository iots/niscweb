from django.conf.urls import url

urlpatterns = [
    url(r'^list/','history.views.history', name='history'),
]
