from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def input(request):
    return render(request,"base.html")
def add(request):
    try:
        a=request.POST["t1"]
        b=request.POST["t2"]
        c=int(a)
        d=int(b)
        e=c+d
        return HttpResponse("the sum is : " +str(e))
    except(ValueError):
        return HttpResponse("Invalid input")

