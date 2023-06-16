from django.shortcuts import render ,redirect
from django.contrib.auth import login ,logout ,authenticate
from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from accounts.forms import NewUserForm
from accounts.models import EmailOrUsernameModelBackend 

# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            username = request.POST['username']
            password = request.POST['password']
            #email = request.POST['email']
            user = EmailOrUsernameModelBackend.authenticate(username, password)
            if user is not None:
                login(request, user)
                return redirect('/')    
        form = AuthenticationForm()
        context ={'form': form}    
        return render(request, 'accounts/login.html',context)
    else:
        return redirect('/')
    
@login_required
def logout_view(request):
   logout(request)
   return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = NewUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        form = NewUserForm()
        contex ={'form': form}
        return render(request, 'accounts/signup.html',contex) 
    else:
        return redirect('/')