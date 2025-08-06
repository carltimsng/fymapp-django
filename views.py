import requests
from django.conf import settings
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def test_view(request):
    return render(request, 'test.html')

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = CustomAuthenticationForm

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
        
        try:
            # Fixed the line below and added timeout
            response = requests.post(
                'https://www.google.com/recaptcha/api/siteverify',
                data=data,
                timeout=5  # Add timeout to prevent hanging
            )
            result = response.json()
        except (requests.RequestException, ValueError) as e:
            # Handle network or JSON errors
            form.add_error(None, 'Security check failed. Please try again.')
            return self.form_invalid(form)

        # Check reCAPTCHA success and score
        if not result.get('success') or result.get('score', 0) < 0.5:
            error_message = result.get('error-codes', ['Unknown error'])[0]
            form.add_error(None, f'Security verification failed: {error_message}')
            return self.form_invalid(form)

        # Process "Remember Me"
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)  # Browser-length session

        return super().form_valid(form)

