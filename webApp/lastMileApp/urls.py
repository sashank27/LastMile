from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sendMail/$', views.sendMail, name='sendMail'),
    url(r'^reschedule_test/$', views.reschedule_test, name='reschedule_test'),
    url(r'^reschedule/(?P<bookingRef>\w+)/$', views.reschedule, name='reschedule'),
    url(r'^claimed/$', views.claimed, name='claimed'),
]