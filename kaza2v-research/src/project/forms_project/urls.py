# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:14:28 2020

@author: Sreemanth Tirumala
"""

from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns =[
    url(r'^$', views.index, name='home'),
    url(r'^output$', views.output,name='output'),
    url(r'^report$', views.report,name='report'),
]
urlpatterns += staticfiles_urlpatterns()