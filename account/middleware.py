from django.shortcuts import redirect

class RedirectMiddleware:
    """
    Middleware to redirect users to the login page if they're not authenticated.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated or already on the login page
        if not request.user.is_authenticated and request.path != '/account/login/':
            return redirect('login')
        return self.get_response(request)
