from django.urls import path
from . import views

app_name = "championships"
urlpatterns = [
    # Championship
    path("",                 views.ChampionshipListView.as_view(), name="list"),
    path("create/",          views.ChampionshipCreateView.as_view(), name="create"),
    path("update/<int:pk>/",  views.ChampionshipUpdateView.as_view(), name="update"),
    path("detail/<int:pk>/",  views.ChampionshipDetailView.as_view(), name="detail"),
    path("delete/<int:pk>/",  views.ChampionshipDeleteView.as_view(), name="delete"),

    # Results
    path("detail/<int:pk>/results/",  views.ChampionshipDetailView.as_view(
        template_name='championships/driversubcategoryposition_list.html'
    ), name="results-list"),
    path("detail/<int:pk>/results/create/",  views.DriverSubCategoryPositionCreateView.as_view(), name="results-create"),
    path("detail/<int:pk>/results/update/<int:result_pk>/",  views.DriverSubCategoryPositionUpdateView.as_view(), name="results-update"),
]
