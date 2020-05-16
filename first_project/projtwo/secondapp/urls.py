from django.conf.urls import url
from secondapp import views

urlpatterns = [
    url(r'^$',views.help,name='help')
    ]
