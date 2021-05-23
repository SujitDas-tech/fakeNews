from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE

def button(request):
    return render(request,'home.html')
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def external(request):
    Title= request.POST.get('title')
    Author= request.POST.get('author')
    Text= request.POST.get('maintext')
    out= run([sys.executable,'C:\\Users\\sujit\\Desktop\\model\\django\\buttonpython\\buttonpython\\pro.py',Title,Author,Text],shell=False,stdout=PIPE)
    print(out)
    output=out.stdout
    output=output[0:(len(output)-2)]
    return render(request,'home.html',{'data1':output})