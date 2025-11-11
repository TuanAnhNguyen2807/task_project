from django.urls import path
from .views import RegisterView, LoginView, MeView, LogoutView

urlpatterns = [
    path("api/register/", RegisterView.as_view(), name="register"),
    path("api/login/", LoginView.as_view(), name="login"),
    path("api/me/", MeView.as_view(), name="me"),
    path("api/logout/", LogoutView.as_view(), name="logout"),
]
