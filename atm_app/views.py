from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    if request.method == 'POST':
       
        try:
            user=User.objects.get(username=request.POST['username'])
            if user.username == request.POST['username'] and user.pin == request.POST['pin']:
                
                msg = 'Welcome in ATM'
                return render(request,'index.html',{'msg':msg,'user':user})

        except:
            msg='username and pin are wrong'
            return render(request,'index.html',{'msg':msg})
    else:
        return render(request,'index.html')

#def Exit(request):
    if 'username' in session :
        username.session.delete()
    return render(request,'index.html')