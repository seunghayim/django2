from django.urls import reverse
from django.shortcuts import redirect


class ProfileSetupMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # login여부 nickname 작성 여부 , url 이 profile-set인지 확인
        if (
            request.user.is_authenticated and
            not request.user.nickname and
            request.path_info != reverse('profile-set')
        ):
            return redirect('profile-set')

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
