from django.shortcuts import redirect
from django.urls import reverse

class AdminLoginRequiredMiddleware:
    """
    Middleware that redirects all requests to /admin/login/ unless user is authenticated
    and is staff (admin).
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Allow access to admin login/logout URLs and static files
        if request.path.startswith(reverse('admin:login')) or request.path.startswith('/static/'):
            return self.get_response(request)

        # If user is not authenticated or not staff, redirect to admin login
        if not request.user.is_authenticated or not request.user.is_staff:
            return redirect(reverse('admin:login'))

        # Otherwise, proceed normally
        return self.get_response(request)
