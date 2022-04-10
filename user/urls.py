from django.urls import path
from . import views

app_name = "user" 

urlpatterns = [
    path("register", views.register_request, name="register"),
    path("login", views.login, name="login"),
]