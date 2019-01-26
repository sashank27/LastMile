from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sendMail/$', views.sendMail, name='sendMail'),
    url(r'^reschedule/(?P<bookingRef>\w+)/$', views.reschedule, name='reschedule'),
]