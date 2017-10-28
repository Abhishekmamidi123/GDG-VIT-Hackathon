# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from data.models import Student

def year1(request):
    first = Student.objects.all().filter(year=1)
    context = {'first':first}
    return render(request, 'analyze/stat.html', context)

def year2(request):
    second = Student.objects.all().filter(year=2)
    context = {'second':second}
    return render(request, 'analyze/stat.html', context)

def year3(request):
    third = Student.objects.all().filter(year=3)
    context = {'third':third}
    return render(request, 'analyze/stat.html', context)

def year4(request):
    fourth = Student.objects.all().filter(year=4)
    context = {'fourth':fourth}
    return render(request, 'analyze/stat.html', context)

class searchyear(TemplateView):
    template_name = "analyze/searchyear.html"
