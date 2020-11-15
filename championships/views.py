from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView
from .models import Championship, DriverSubCategoryPosition
from .forms import ChampionshipModelForm, DriverSubCategoryPositionForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


class ChampionshipListView(ListView):
    model = Championship


class ChampionshipDetailView(DetailView):
    model = Championship


class ChampionshipCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Championship
    form_class = ChampionshipModelForm
    success_message = "Prvenstvo uspješno stvoreno"


class ChampionshipUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Championship
    form_class = ChampionshipModelForm
    template_name_suffix = '_update_form'
    success_message = "Prvenstvo uspješno ažurirano"

    def get_initial(self):
        initial = super(ChampionshipUpdateView, self).get_initial()
        self.object = self.get_object()
        initial['championship_type'] = self.object.championship_type
        initial['organizer'] = self.object.organizer.name
        return initial
        

class ChampionshipDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Championship
    success_message = "Prvenstvo uspješno izbrisano"
    success_url = "/championships/"


class DriverSubCategoryPositionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = DriverSubCategoryPosition
    form_class = DriverSubCategoryPositionForm
    template_name = "championships/championship_detail.html"
    success_message = "Rezultat uspješno unesen"

    def get_initial(self):
        initial = super(DriverSubCategoryPositionCreateView, self).get_initial()
        initial['championship'] = Championship.objects.get(id=self.kwargs.get('pk'))
        return initial
    
    def get_context_data(self, **kwargs):
        context = super(DriverSubCategoryPositionCreateView, self).get_context_data(**kwargs)
        context["object"] = Championship.objects.get(id=self.kwargs.get('pk'))
        context["championship"] = context["object"]
        return context
    
    def get_success_url(self):
        context = self.get_context_data()
        return context["championship"].get_absolute_url()


class DriverSubCategoryPositionUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = DriverSubCategoryPosition
    form_class = DriverSubCategoryPositionForm
    success_message = "Rezultat uspješno ažuriran"
    template_name = "championships/championship_detail.html"