from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import AccessToken

class ClearExpiredJWTCookiesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        access_token = request.COOKIES.get("access")
        if access_token:
            try:
                AccessToken(access_token)
            except TokenError:
                response.delete_cookie("access")
                response.delete_cookie("refresh")

        return response
