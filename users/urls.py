from django.urls import path
from .views import RegisterView , LogInView
app_name  = "users"


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LogInView.as_view(), name="login"),
    # path("logout/", LogoutView.as_view(), name="logout")
]
