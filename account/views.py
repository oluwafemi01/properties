from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,get_user_model,login,logout
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.models import User
#from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse

from django.http import HttpResponseRedirect, HttpResponse
#from django.urls import reverse
# Create your views here.
from frontend.views import index,register
def Login_view(request):
    if request.method == "POST" :
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username,password=password)
            if not user:
                user_qs = User.objects.filter(email=username)
                if user_qs.count()== 1:
                    for t in user_qs:
                        use = t.username
                    user = authenticate(username=use,password=password)
            login(request,user)
            if not request.user.is_authenticated():
                errormsg = "Username/Password incorrect"
                title= "Error while trying to login"
                return render (request, 'frontend/home.html',{"title":title,"error":errormsg})
            else:
                return redirect("/")
        else:
            errormsg = "Please enter valid input"
            title="Error while trying to login"
    else:
         errormsg = ""
         title="login page"    
    return render (request, 'frontend/home.html',{"title":title,"error":errormsg})    
    

def register_view(request):
    if request.method != "POST" :
        return redirect("/register")
    form = UserRegisterForm(request.POST)
    if form.is_valid():
        user = form.save(commit = False)
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username,password=password)
        if new_user is not None :
            login(request,new_user)
            return redirect("/")
    else:
        title="Registration page"
        errormsg = "Invalid input fields"
    return render (request, 'frontend/register.html',{"title":title,"error":errormsg})

def logout_view(request):
    logout(request)
    return redirect("/")
    
