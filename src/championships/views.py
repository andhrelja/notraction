from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from .forms import ChampionshipModelForm, DriverSubCategoryPositionForm
from .models import (
    Category, 
    Championship, 
    DriverSubCategoryPosition, 
    CATEGORY_CHOICES
)

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


class ChampionshipListView(ListView):
    model = Championship

    def get_context_data(self, **kwargs):
        context = super(ChampionshipListView, self).get_context_data(**kwargs)
        now = timezone.now()
        min_year = Championship.objects.earliest('start_date').start_date.year
        context.update({
            'years': (year for year in range(now.year, min_year-1, -1)),
            'year_today': now.year,
            'categories': Category.objects.filter(~Q(name=4))
        })
        return context
    


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
        initial['organizer'] = self.object.organizer.name
        return initial
    

class ChampionshipDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Championship
    success_message = "Prvenstvo uspješno izbrisano"
    success_url = "/championships/"


class DriverSubCategoryPositionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = DriverSubCategoryPosition
    form_class = DriverSubCategoryPositionForm
    template_name = "championships/driversubcategoryposition_list.html"
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
        return context["championship"].get_results_url()
    
    def form_invalid(self, form):
        return super().form_invalid(form)


class DriverSubCategoryPositionUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = DriverSubCategoryPosition
    form_class = DriverSubCategoryPositionForm
    success_message = "Rezultat uspješno ažuriran"
    template_name = "championships/driversubcategoryposition_update_list.html"
    
    def get_initial(self):
        initial = super(DriverSubCategoryPositionUpdateView, self).get_initial()
        initial['championship'] = Championship.objects.get(id=self.kwargs.get('championship_pk'))
        return initial
            
    def get_context_data(self, **kwargs):
        context = super(DriverSubCategoryPositionUpdateView, self).get_context_data(**kwargs)
        context["object"] = Championship.objects.get(id=self.kwargs.get('championship_pk'))
        context["championship"] = context["object"]
        return context
    
    def get_success_url(self):
        context = self.get_context_data()
        return context["championship"].get_results_url()