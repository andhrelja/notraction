from django.contrib.auth.forms import AuthenticationForm
from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("login/",          views.LoginView.as_view(), name="login"),
    path("register/",       views.ProfileCreateView.as_view(), name="create"),
    path("update/<int:pk>/",  views.ProfileUpdateView.as_view(), name="update"),
    path("detail/<int:pk>/",  views.ProfileDetailView.as_view(), name="detail"),
    path("delete/<int:pk>/",  views.ProfileDeleteView.as_view(), name="delete"),
]
