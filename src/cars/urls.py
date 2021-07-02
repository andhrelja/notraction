from django.urls import path
from . import views

app_name = "cars"
urlpatterns = [
    path("",                views.CarListView.as_view(), name="list"),
    path("create/<int:driver_pk>", views.CarCreateView.as_view(), name="create"),
    path("update/<int:pk>/",  views.CarUpdateView.as_view(), name="update"),
    path("detail/<int:pk>/",  views.CarDetailView.as_view(), name="detail"),
    path("delete/<int:pk>/",  views.CarDeleteView.as_view(), name="delete"),
]
