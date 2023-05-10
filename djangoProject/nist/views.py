from django.shortcuts import render
def home(request):
    info={'name':'htet','age':22,'hobby':'reading'}
    return render(request, 'home.html',{'name': info})



# Create your views here.
