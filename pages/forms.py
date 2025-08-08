from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    remember_me = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.CheckboxInput(),
        label='Remember me for 30 days'
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Email'
        self.fields['username'].widget.attrs.update({
            'autocomplete': 'email',
            'placeholder': 'your.email@example.com'
        })
        self.fields['password'].widget.attrs.update({
            'autocomplete': 'current-password',
            'placeholder': '••••••••'
        })

class SignupForm(forms.Form):
    email = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email',
            'class': 'form-control',
            'autocomplete': 'email',
        }),
    )
