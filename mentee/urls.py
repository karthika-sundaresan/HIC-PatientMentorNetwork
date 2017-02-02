from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from mentee.models import Mentee

from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
	url(r'^$', ListView.as_view(queryset=Mentee.objects.all(), 
	                         template_name="mentee/mentee.html")),
]