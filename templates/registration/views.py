from django.contrib.auth.views import LoginView
from django.conf import settings
import requests
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    remember_me = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.CheckboxInput(),
        label='Remember me for 30 days'
    )

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = CustomAuthenticationForm
    authentication_form = None

    def form_valid(self, form):
        # Verify reCAPTCHA
        recaptcha_response = self.request.POST.get('g-recaptcha-response')
        
        if not recaptcha_response:
            form.add_error(None, 'Security verification failed. Please try again.')
            return self.form_invalid(form)
        
        # Verify with Google
        data = {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': recaptcha_response
        }
        response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = response.json()
        
        # Check reCAPTCHA success and score
        if not result.get('success') or result.get('score', 0) < 0.5:
            form.add_error(None, 'Security verification failed. Please try again.')
            return self.form_invalid(form)
        
        # Process "Remember Me"
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)  # Browser-length session
        
        return super().form_valid(form)
