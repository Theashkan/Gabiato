from django import forms
from django.contrib.auth.models import User
from accounts.models import UserProfile

class UserRrgisterForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', "email", "password2")
        widgets = {
            'first_name': forms.TextInput(attrs={"class": "form-control"}),
            'last_name': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'username': forms.TextInput(attrs={"class": "form-control"}),
            'password': forms.PasswordInput(attrs={"class": "form-control"}),
        }
        help_texts = {
            'password2' : ('Retype your password')
        }
    def clean(self):
        cleaned_data = super(UserRrgisterForm, self).clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password != password2:
            raise forms.ValidationError(
                "password arent match"
            )


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length = 150, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control form-control-lg"}))
    
class EditDashboardForm(forms.ModelForm):
    first_name = forms.CharField(max_length = 150, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    last_name = forms.CharField(max_length = 150, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', "about", 'image')
        widgets = {
                    'about' : forms.Textarea(attrs={'class': 'form-control form-control-lg', 'rows':3, 'cols':5}),
                    'image' : forms.FileInput(attrs={"class": "form-control form-control-lg"}),


        }
