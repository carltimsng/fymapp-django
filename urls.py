from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views  # Add this if not already imported

admin.site.site_url = '/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fymapp.urls')),  # Include your app's URLs
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # ← COMMA added here
    path('auth/', include('social_django.urls', namespace='social')),       # ← Social auth route
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

