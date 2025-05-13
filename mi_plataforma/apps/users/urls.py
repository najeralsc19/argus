from django.urls import path
from .views import registro, login_view

app_name = "users"

urlpatterns = [
    path("registro/", registro, name="registro"),  # URL para el formulario de registro
    path("login/", login_view, name="login"),  # URL para el formulario de login
]