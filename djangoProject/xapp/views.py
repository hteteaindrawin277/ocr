import json

from django.shortcuts import render
def login(request):
        return render(request,'login.html')
dict={}
def nextpage(request):


        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        dict.update({len(dict):{'name':username,'email':email,'password':password}})
        f = open('userdb.json','w')
        f.write(json.dumps(dict))
        f.close()
        print('vjhvh')
        info={'name':username,'email': email,'password':password}
        return render(request,'nextpage.html',{'info':info})
    #return render(request,'login.html')
# Create your views here.

def seclogin(request):
    return render(request,'seclogin.html')

def comparedata(request):
        with open('userdb.json') as f:
                data=json.load(f)
                useremail=request.POST['email']
                userpassword=request.POST['password']
                for i in data:
                        email=data.get(f'{i}').get('email')
                        password=data.get(f'{i}').get('password')
                        if useremail == email and userpassword == password:
                                return render(request,'success.html')
                        else:
                                return render(request,'login.html')