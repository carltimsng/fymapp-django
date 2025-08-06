from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_url = '/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fymapp.urls')),  # Include your app's URLs
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
