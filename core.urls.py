from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Your app URLs here, e.g.:
    path('', include('pages.urls')),  # or whatever your main app is called

    # Add this line to include social_django URLs with namespace 'social'
    path('auth/', include('social_django.urls', namespace='social')),
]

