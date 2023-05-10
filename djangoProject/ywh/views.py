from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def form(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        data={'fname':fname,'lname':lname}
        return render(request,'ywhform.html',data)
    return render(request,'ywhform.html')

def next(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        data={'fname':fname,'lname':lname}
    return render(request,'next.html',data)