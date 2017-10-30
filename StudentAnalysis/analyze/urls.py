from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = "analyze"

urlpatterns = [
    url(r'^searchyear/', views.searchyear.as_view(), name="searchyear"),
    url(r'^one/', views.year1, name="year1"),
    url(r'^two/', views.year2, name="year2"),
    url(r'^three/', views.year3, name="year3"),
    url(r'^four/', views.year4, name="year4"),
    url(r'^(?P<year>[0-9]+)/(?P<rollno>[0-9]+)/$', views.stat, name="stat"),
    url(r'^(?P<year>[a-z]+)/$', views.classAnalysis, name="classanalysis"),
]
