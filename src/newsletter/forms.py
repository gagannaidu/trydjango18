from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['email','full_name']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')
        if not domain =='USC':
            raise forms.ValidationError("Please make sure you use your USC email")
        if not extension == 'edu':
            raise forms.ValidationError("Please use a valid .edu email")
        return email
        
        