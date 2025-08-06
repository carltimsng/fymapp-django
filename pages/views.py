from django.shortcuts import render

# Main pages
def home(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

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

