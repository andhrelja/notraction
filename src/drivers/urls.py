from django.urls import path
from . import views

app_name = "drivers"
urlpatterns = [
    path("",                  views.DriverListView.as_view(), name="list"),
    path("create/",           views.DriverCreateView.as_view(), name="create"),
    path("update/<int:pk>/",  views.DriverUpdateView.as_view(), name="update"),
    path("detail/<int:pk>/",  views.DriverDetailView.as_view(), name="detail"),
    path("delete/<int:pk>/",  views.DriverDeleteView.as_view(), name="delete"),
]
