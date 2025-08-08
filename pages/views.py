from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django import forms
from .forms import CustomAuthenticationForm
import requests
from django.conf import settings

# Main pages
def home(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def signup(request):
    class SignupForm(forms.Form):
        email = forms.EmailField(
            label='Email Address',
            widget=forms.EmailInput(attrs={
                'placeholder': 'Enter your email',
                'autocomplete': 'email',
                'required': True,
                'class': 'form-control',
            }),
        )

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            print(f"New signup email: {email}")
            # TODO: send verification email

            return render(request, 'pages/signup_success.html', {'email': email})
    else:
        form = SignupForm()
    return render(request, 'pages/signup.html', {'form': form})

def create_profile(request):
    return render(request, 'create_your_profile.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def profile_about_us(request):
    return render(request, 'profile.html')

def privacy(request):
    return render(request, 'privacy.html')

def terms(request):
    return render(request, 'terms.html')

def faq(request):
    return render(request, 'faq.html')

def contact(request):
    return render(request, 'contact.html')

# Dashboard pages
def notification_preferences(request):
    return render(request, 'notification_preferences.html')

def privacy_settings(request):
    return render(request, 'privacy_settings.html')

def my_profile_edit(request):
    return render(request, 'my_profile_edit.html')

def create_hot_date(request):
    return render(request, 'create_hotdate.html')

def messages(request):
    return render(request, 'messages.html')

def account_settings(request):
    return render(request, 'account_settings.html')

def hot_dates_full_list(request):
    return render(request, 'hot_dates_full_list.html')

# ADD the custom login view class
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
            response = requests.post(
                'https://www.google.com/recaptcha/api/siteverify',
                data=data, timeout=5
            )
            result = response.json()
        except (requests.RequestException, ValueError) as e:
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

