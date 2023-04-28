from inertia import share
from django.conf import settings


class InertiaShareMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        share(request,
              # app_name=settings.APP_NAME,
              user=lambda: request.user,
              authenticated=lambda: request.user.is_authenticated,
              )
        response = self.get_response(request)
        return response
