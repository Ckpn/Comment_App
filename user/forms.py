from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,PasswordChangeForm
from django import forms
from django.forms import widgets
from django.contrib.auth.models import User

class UyeGirisiForm(AuthenticationForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class']= 'form-control w-50'
#       self.fields['username'].widget = widgets.TextInput(attrs={'class':'form-control'})
        self.fields['password'].widget= widgets.PasswordInput(attrs={'class':'form-control w-50'})
        
        
class UyeKayitForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget = widgets.TextInput(attrs={'class':'form-control w-50 '})
        self.fields['first_name'].widget = widgets.TextInput(attrs={'class':'form-control w-50'})
        self.fields['last_name'].widget = widgets.TextInput(attrs={'class':'form-control w-50'})
        self.fields['email'].widget = widgets.EmailInput(attrs={'class':'form-control w-50'})
        self.fields['password1'].widget = widgets.PasswordInput(attrs={'class':'form-control w-50'})
        self.fields['password2'].widget = widgets.PasswordInput(attrs={'class':'form-control w-50'})
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email = email).exists():
            self.add_error('email','Bu mail kullanılıyor. Başka bir mail adresi giriniz')
            return email

class SifreDegistir(PasswordChangeForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['old_password'].widget = widgets.PasswordInput(attrs={'class':'form-control w-50'})
        self.fields['new_password1'].widget = widgets.PasswordInput(attrs={'class':'form-control w-50'})
        self.fields['new_password2'].widget = widgets.PasswordInput(attrs={'class':'form-control w-50'})