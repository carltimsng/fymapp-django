from django.contrib import admin
from django.urls import path, include  # <-- include added here
from django.contrib.auth import views as auth_views
from core import views as core_views
from pages import views as pages_views
from pages.views import CustomLoginView

admin.site.site_url = '/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
    path('about-us/', pages_views.aboutus, name='aboutus'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', pages_views.signup, name='signup'),
    path('create-profile/', pages_views.create_profile, name='create_profile'),
    path('dashboard/', pages_views.dashboard, name='dashboard'),
    path('profile-about-us/', pages_views.profile_about_us, name='profile_about_us'),
    path('privacy/', pages_views.privacy, name='privacy'),
    path('terms/', pages_views.terms, name='terms'),
    path('faq/', pages_views.faq, name='faq'),
    path('contact/', pages_views.contact, name='contact'),
    path('notification-preferences/', pages_views.notification_preferences, name='notification_preferences'),
    path('privacy-settings/', pages_views.privacy_settings, name='privacy_settings'),
    path('my-profile-edit/', pages_views.my_profile_edit, name='my_profile_edit'),
    path('create-hot-date/', pages_views.create_hot_date, name='create_hot_date'),
    path('messages/', pages_views.messages, name='messages'),
    path('account-settings/', pages_views.account_settings, name='account_settings'),
    path('hot-dates-full-list/', pages_views.hot_dates_full_list, name='hot_dates_full_list'),

    # Password reset
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='registration/password_reset_form.html',
             email_template_name='registration/password_reset_email.html',
             subject_template_name='registration/password_reset_subject.txt'
         ),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    # ✅ ADD THIS LINE FOR SOCIAL LOGIN
    path('auth/', include('social_django.urls', namespace='social')),
]

