from django.urls import path
from . import views

app_name = "championships"
urlpatterns = [
    path("",                views.ChampionshipListView.as_view(), name="list"),
    path("create/",         views.ChampionshipCreateView.as_view(), name="create"),
    path("update/<int:pk>/",  views.ChampionshipUpdateView.as_view(), name="update"),
    path("detail/<int:pk>/",  views.ChampionshipDetailView.as_view(), name="detail"),
    path("delete/<int:pk>/",  views.ChampionshipDeleteView.as_view(), name="delete"),
]
