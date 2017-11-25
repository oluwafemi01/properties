from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.models import User

user = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    def clean(self,*args,**kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username,password=password)
            if not user:
                user_qs = User.objects.filter(email=username)
                if user_qs.count()== 1:
                    for t in user_qs:
                        use = t.username
                    user = authenticate(username=use,password=password)
                    if not user:
                       raise forms.ValidationError("This user does not exit") 
                else:
                    raise forms.ValidationError("This user does not exit")              
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
            if not user.is_active:
                raise forms.validationError("This user is not longer active")
        return super(UserLoginForm,self).clean(*args,**kwargs)
    
class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
                'username',
                'email',
                'password'
            ]
        def clean_email(self):
            email = self.cleaned_data.get('email')
            email_qs = User.objects.filter(email = email)
            if email_qs.exits():
                raise forms.validationError("this email has already been registered")
            return email

        def clean_username(self):
            username = self.cleaned_data.get('username')
            username_qs = User.objects.filter(username = username)
            if username_qs.exits():
                raise forms.validationError("this username has already been registered")
            return username