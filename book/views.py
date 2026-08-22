from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET,require_POST
from . import forms

def loginView(request):
    
    if request.method=="POST":
        
        form = forms.LoginForm(request,data=request.POSST or None)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
        else:
            return redirect("books:login_view")
        
    else:
        form = forms.LoginForm()
        context = {
            "title":"ログイン画面",
            "form":form
        }
        return render(request,"books/login.html",context)

