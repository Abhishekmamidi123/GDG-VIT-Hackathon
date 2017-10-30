# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from data.models import Student
import json
def year1(request):
    first = Student.objects.all().filter(year=1)
    context = {'list':first, 'year':'first'}
    return render(request, 'analyze/list.html', context)

def year2(request):
    second = Student.objects.all().filter(year=2)
    context = {'list':second, 'year':'second'}
    return render(request, 'analyze/list.html', context)

def year3(request):
    third = Student.objects.all().filter(year=3)
    context = {'list':third, 'year':'third'}
    return render(request, 'analyze/list.html', context)

def year4(request):
    fourth = Student.objects.all().filter(year=4)
    context = {'list':fourth, 'year':'fourth'}
    return render(request, 'analyze/list.html', context)

class searchyear(TemplateView):
    template_name = "analyze/searchyear.html"

def stat(request,year,rollno):
    obj = Student.objects.all().filter(year=year).filter(rollno=rollno)
    list1 = [obj[0].name,obj[0].score,obj[0].workshops,obj[0].interns,obj[0].clubs,obj[0].eventsorganized]
    context = {'list1':json.dumps(list1), 'name':list1[0]}
    return render(request, 'analyze/stat.html', context)

def classAnalysis(request,year):
    if str(year)=='first':
        y=1
    elif str(year)=='second':
        y=2
    if str(year)=='third':
        y=3
    if str(year)=='fourth':
        y=4
    obj = Student.objects.all().filter(year=y)
    t = Student.objects.all().filter(year=y)
    l = len(t)
    avg=0
    wavg=0
    iavg=0
    cavg=0
    aavg=0
    for x in t:
        avg=avg+x.score
        wavg=wavg+x.workshops
        iavg=iavg+x.interns
        cavg=cavg+x.clubs
        aavg=aavg+x.eventsorganized
    avg = avg/l
    wavg = (wavg*100)/(l*4)
    iavg = (iavg*100)/(l*2)
    cavg = (cavg*100)/(l*3)
    aavg = (aavg*100)/(l*2)
    context = {'avg':avg,'wavg':wavg,'iavg':iavg, 'cavg':cavg, 'aavg':aavg}
    return render(request, 'analyze/classanalysis.html', context)


# x=np.array([[89,3,1,2,0],[65,3,2,1,1],[54,0,0,2,2],[57,0,2,3,1],[75,1,0,0,2],[82,0,1,0,2],[87,1,1,2,2],[92,0,0,0,2],[52,0,1,3,1],[67,2,2,3,2],[76,3,2,2,1],[79,1,1,0,0],[83,1,1,1,2],[63,1,2,1,1],[78,3,0,2,1]])
# y=np.array([1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0])
# model = GaussianNB()
# model.fit(x, y)
# predicted= model.predict([[1,2],[3,4]])
# print predicted
