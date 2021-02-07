# I have careted this is file name ->  Aashish Panchal
from django.http import HttpResponse
from django.shortcuts import render
import re

def index(request):
    return render(request=request, template_name='index.html')

def removePunc(text=''):
    '''This function is removed all punctuations of string'''
    data = re.sub(r"[^\w\s]", '', text)
    return data

def analyze(request):
    text = request.POST.get("text", "default")
    remPunc = request.POST.get("removepunc", "off")
    uppercase = request.POST.get("uppercase", "off")
    lowercase = request.POST.get("lowercase", "off")
    space= request.POST.get("removespace", "off")
    char = request.POST.get("total-char", "off")

    analyze_text = ""
    uppertext = ""
    lowertext = ""
    totalChar = ""
    fullanalyze_text = ""
    remSpaceText = ""

    if remPunc == "on":
        analyze_text = removePunc(text)
        fullanalyze_text=analyze_text

    if uppercase == "on":
        uppertext = text.upper()
        fullanalyze_text = fullanalyze_text.upper()
        
    if lowercase == "on":
        lowertext = text.lower()
        fullanalyze_text = fullanalyze_text.lower()

    if space == "on":
        remSpaceText = re.sub(' +', ' ', text)
        fullanalyze_text=re.sub(' +', ' ', fullanalyze_text)

    if char == "on":
        totalChar = str(len(text))
    
    params = {'analyzed_text': analyze_text, 'text':text, "upper":uppertext, "lower":lowertext, "space": remSpaceText, "char":totalChar, "fullanalyze":fullanalyze_text}
    
    return render(request, 'analyze.html', params)