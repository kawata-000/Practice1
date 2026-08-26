from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET,require_POST
from . import forms
from django.core.paginator import Paginator
from .models import BookList


def loginView(request):
    
    if request.method=="POST":
        
        form = forms.LoginForm(request,data=request.POST or None)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect("book:bookList_view")
        else:
            return redirect("books:login_view")
        
    else:
        form = forms.LoginForm()
        context = {
            "title":"ログイン画面",
            "form":form
        }
        return render(request,"book/login.html",context)
    
def UserRegisterView(request):
    
    if request.method == "POST":
        
        form = forms.UserRegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("book:login_view")
        
    else:
        form = forms.UserRegisterForm()
            
        context = {
            "title":"ユーザー登録",
            "form":form
        }
        return render(request,"book/userRegister.html",context)
    
@login_required
def bookListView(request):
    
    if request.method == "POST":
        
        pass
    
    else:
        
        book = BookList.objects.all()
        paginator = Paginator(book,10)
        page_number = request.GET.get("page")
        books_object = paginator.get_page(page_number)
        
        context = {
            "title":"一覧ページ",
            "books_page_obj":books_object
        }
        
        return render(request,"book/booklist.html",context)
        
        
        

