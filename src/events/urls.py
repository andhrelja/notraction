from django.urls import path
from . import views

app_name = "events"
urlpatterns = [
    path("",                views.EventListView.as_view(), name="list"),
    path("create/",         views.EventCreateView.as_view(), name="create"),
    path("update/<int:pk>/",  views.EventUpdateView.as_view(), name="update"),
    path("detail/<int:pk>/",  views.EventDetailView.as_view(), name="detail"),
    path("delete/<int:pk>/",  views.EventDeleteView.as_view(), name="delete"),
]
