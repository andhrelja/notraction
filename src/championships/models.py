from django.db import models
from django.shortcuts import reverse
from django.conf import settings
from drivers.models import DriverSubCategoryPosition


CATEGORY_CHOICES = (
    (1, 'Brdo'),
    (2, 'Formula Driver'),
    (3, 'Drift'),
    (4, 'Općenito'),
)

# Create your models here.
class Championship(models.Model):

    # General
    name        = models.CharField("Naziv", max_length=64)
    description = models.TextField("Opis", null=True, blank=True)
    location    = models.CharField("Lokacija", max_length=96)
    image       = models.ImageField("Slika", null=True, blank=True, upload_to='champtionships/images/')

    # Date & Time
    start_date  = models.DateField("Datum početka")
    end_date    = models.DateField("Datum završetka")

    # Foreign keys
    city        = models.ForeignKey(
        "events.City", verbose_name="Grad", on_delete=models.CASCADE)
    organizer   = models.ForeignKey(
        "championships.Organizer", verbose_name="Organizator", on_delete=models.CASCADE)
    albums      = models.ManyToManyField("gallery.Gallery", verbose_name="Albumi")
    category    = models.ForeignKey(
        "championships.Category", on_delete=models.CASCADE)

    class Meta:
        ordering = ['start_date']
        verbose_name = "Prvenstvo"
        verbose_name_plural = "Prvenstva"

    @property
    def location_name(self):
        if self.location != self.city.name:
            location_name = "{location} - {city}, {county}".format(
                location=self.location, city=self.city, county=self.city.county)
        else:
            location_name = "{city}, {county}".format(
                city=self.city, county=self.city.county)
        return location_name.strip()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("championships:detail", kwargs={"pk": self.pk})
    
    def get_results_url(self):
        return reverse("championships:results-list", kwargs={"pk": self.pk})


class Category(models.Model):
    # General
    name = models.IntegerField(
        "Naziv kategorije", choices=CATEGORY_CHOICES, default=4)

    class Meta:
        verbose_name = "Kategorija"
        verbose_name_plural = "Kategorije"

    def __str__(self):
        return self.get_name_display()


class SubCategory(models.Model):

    # General
    name = models.CharField(
        "Naziv kategorije", default="Općenito", max_length=64)
    active = models.BooleanField("Aktivna podkategorija", default=True)

    # Foreign keys
    category = models.ForeignKey(
        "championships.Category", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Podkategorija"
        verbose_name_plural = "Podkategorije"

    def results(self, championship):
        return DriverSubCategoryPosition.objects.filter(subcategory=self, championship=championship)

    def top_results(self, championship):
        return DriverSubCategoryPosition.objects.filter(subcategory=self, championship=championship, position__lte=3)
    
    def driver_results(self, driver):
        return DriverSubCategoryPosition.objects.filter(subcategory=self, driver=driver)
    
    def __str__(self):
        return self.name

class Organizer(models.Model):

    name = models.CharField("Naziv", max_length=64)

    class Meta:
        verbose_name = "Organizator"
        verbose_name_plural = "Organizatori"

    def __str__(self):
        return self.name
