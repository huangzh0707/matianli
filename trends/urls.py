from django.conf.urls import url

from . import views

app_name = 'trends'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<company_id>[0-9]+)/$', views.profile, name='profile'),

]