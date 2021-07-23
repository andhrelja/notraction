from django.urls import path
from . import views

app_name = "gallery"
urlpatterns = [
    path("create/<int:championship_pk>/", views.GalleryCreateView.as_view(), name="create"),
    path("",                  views.GalleryListView.as_view(), name="list"),
    path("update/<int:pk>/",  views.GalleryUpdateView.as_view(), name="update"),
    path("detail/<int:pk>/",  views.GalleryDetailView.as_view(), name="detail"),
    path("delete/<int:pk>/",  views.GalleryDeleteView.as_view(), name="delete"),
]
