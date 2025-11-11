from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        from django.contrib.auth import authenticate

        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            response = Response({
                "message": "Login successful",
                "user": {"id": user.id, "username": user.username}
            })

            # Save tokens in cookies (HttpOnly)
            response.set_cookie(
                key="access",
                value=str(refresh.access_token),
                httponly=True,
                secure=True,
                samesite="Lax",
                max_age=3600,
            )
            response.set_cookie(
                key="refresh",
                value=str(refresh),
                httponly=True,
                secure=True,
                samesite="Lax",
                max_age=7 * 24 * 3600,
            )

            return response
        return Response({"error": "Invalid credentials"}, status=400)


class MeView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class LogoutView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        response = Response({"message": "Logged out successfully"}, status=200)
        response.delete_cookie("access")
        response.delete_cookie("refresh")
        return response
    