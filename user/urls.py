from django.urls import path
from .views import home,login
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", home, name="home"),
    path("login", login, name="login"),
    path('logouts/', LogoutView.as_view(),name="logout_app"),
]