from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
import re
from .models import BookList
class LoginForm(AuthenticationForm):
    
    username = forms.CharField(
        required=True,
        error_messages={
            "required":"ユーザー名は必須入力です",
        },
        widget=forms.TelInput(
            {"class":"username_input","placeholder":"ユーザー名"}
        )
    )
    password = forms.CharField(
        required=True,
        error_messages={
            "required":"パスワードは必須入力です",
        },
        widget=forms.PasswordInput(
            {"class":"username_input","placeholder":"ユーザー名"}
        )
    )
    

class UserRegisterForm(UserCreationForm):
    use_required_attribute = True
    
    username = forms.CharField(
        required=True,
        label="ユーザー名",
        error_messages={
            "required":"必須入力です"
        },
        widget=forms.TelInput(
            attrs={"class":"username_input","placeholder":"ユーザー名"}
        )
    )
    email = forms.EmailField(
        required=True,
        label="メールアドレス",
        error_messages={
            "required":"必須入力です"
        },
        widget=forms.EmailInput(
            attrs={"class":"email_input","placeholder":"xxx@co,jp"}
        )
    )
    password1 = forms.CharField(
        required=True,
        label="パスワード",
        error_messages={
            "required":"必須入力です"
        },
        widget=forms.PasswordInput(
            attrs={"class":"password1_input"}
        )
    )
    password2 = forms.CharField(
        required=True,
        label="確認用パスワード",
        error_messages={
            "required":"必須入力です"
        },
        widget=forms.TelInput(
            attrs={"class":"password2_input"}
        )
    )
    
    def clean_email(self):
        
        email = self.cleaned_data.get("email")
        pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        
        if not re.match(pattern,email):
            raise forms.ValidationError("メールアドレスに使用できない文字が使用されています")
        
        return email
    
    def clean(self):
        
        clean_data = super().clean()
        
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        
        if password1 != password2:
            self.add_error(None,"パスワードと確認用パスワードが異なっています")
            
        return self.cleaned_data
            
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
                
