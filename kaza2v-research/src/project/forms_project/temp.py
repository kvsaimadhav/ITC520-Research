# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 23:21:27 2020

@author: Sreemanth Tirumala
"""

def form_two(request):
    if request.method == "POST":
        data=None
        if request.method=="GET":
            fname=request.GET.get('fname')
            lname=request.GET.get('lname')
            id_x=request.GET.get('id')
            zip_code=request.GET.get('zip')
            email=request.GET.get('email')
            date=request.GET.get('date')
            bug=request.GET.get('bug_type')
            bug_prev=request.GET.get('previous-report')
            print(fname)
            print(lname)
            print(id_x)
            print(bug)
            print(bug_prev)
    else:
        print('FUCK YOU')
    