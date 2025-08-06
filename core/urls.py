from django.contrib import admin
from django.urls import path
from pages import views  # Make sure 'pages' is your app name

admin.site.site_url = '/'

urlpatterns = [
    path('admin/', admin.site.urls),

    # Main pages
    path('', views.home, name='home'),
    path('about-us/', views.aboutus, name='aboutus'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('create-profile/', views.create_profile, name='create_profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile-about-us/', views.profile_about_us, name='profile_about_us'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),

    # Dashboard pages
    path('notification-preferences/', views.notification_preferences, name='notification_preferences'),
    path('privacy-settings/', views.privacy_settings, name='privacy_settings'),
    path('my-profile-edit/', views.my_profile_edit, name='my_profile_edit'),
    path('create-hot-date/', views.create_hot_date, name='create_hot_date'),
    path('messages/', views.messages, name='messages'),
    path('account-settings/', views.account_settings, name='account_settings'),
    path('hot-dates-full-list/', views.hot_dates_full_list, name='hot_dates_full_list'),
]

