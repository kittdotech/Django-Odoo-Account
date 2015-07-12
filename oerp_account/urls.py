

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^islogin$', views.islogin, name='islogin'),
    url(r'^odooconnect$', views.odooconnect, name='odooconnect'),
    url(r'^odoologin$', views.odoologin, name='odoologin'),
    url(r'^odooacclst$', views.listaccountcodes, name='odooacclst'),
    url(r'^odooaccnew$', views.odooaccnew, name='odooaccnew'),
    url(r'^odoocreatenew$', views.odoocreatenew, name='odoocreatenew'),
    url(r'^logout$', views.logout, name='logout'),


]