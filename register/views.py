from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from register.forms import NewUser
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def register_req(request):
    if request.method=="POST":
        form = NewUser(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request,"registeration succcess")
        messages.error(request,"registeration unsucccessfull")
    form=NewUser
    return render(request,"register.html",{'register_form':form})

def login_req(request):
    if request.method=="POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/home/?success=1')
            else:
                messages.error(request,"invaild username and password")
        else:
            messages.error(request,"invaild username and password")
    form=AuthenticationForm
    return render(request,"login.html",{'login_form':form})
def home_req(request):
    return render(request,"home.html")
def logout_req(request):
    logout(request)
    return redirect("home")