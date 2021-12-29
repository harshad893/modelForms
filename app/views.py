from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.forms import *
def tf(request):
    T=TopicForm()
    d={'T':T}
    if request.method=='POST':
        FD=TopicForm(request.POST)
        FD.save()
        return HttpResponse('data is inserted')
    return render(request,'TF.html',d)

def wb(request):
    W=WebpageForm()
    d={'W':W}
    return render(request,'WB.html',d)
