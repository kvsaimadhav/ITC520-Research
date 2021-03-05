from django.shortcuts import render
import pickle as pkl
import pandas as pd
import numpy as np
from sklearn import preprocessing
import os
cwd = os.getcwd()

# Create your views here.
from django.http import HttpResponse


def index(request): 
    # render function takes argument  - request 
    # and return HTML as response 
    return render(request, "form_one.html") 

def output(request):
    if request.method == "GET":
            fname=request.GET.get('fname')
            request.session['name'] = fname
            df=pd.read_csv(cwd+'/simulate.csv')
            rand=df.sample(n=1).values
            with open(cwd+'/final_model.sav', 'rb') as file:
                model = pkl.load(file)
            result=model.predict(rand)
            if(result==1):
                return render(request,'captcha.html')
            else:
                return render(request,'form_two.html')
    else:
        return render(request, "error-404.html") 
    
def report(request):
    if request.method == "GET":
        return render(request,'form_two.html')     
    else:
        return render(request, "error-404.html")
            
            
        
        
    
    
    
    
    
    
    
    
                
