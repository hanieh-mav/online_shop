from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password' , widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation' , widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email','first_name','last_name','phone')


    def clean_password2(self):
        cd = self.changed_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise forms.ValidationError('Password must match')
        return cd['password2'] 


    def save(self , commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save() 
        return user         


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    
    class Meta:
        model = User
        fields = ('email','first_name','last_name','phone')


    def clean_password(self):
        return self.initial['password']  


class LoginUserForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))  
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))  


class RegisterUserForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))  
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))  
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))  
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))  
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Password')   
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Password confirmation')  