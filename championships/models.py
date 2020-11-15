from django.db import models
from django.forms.fields import ImageField
from django.shortcuts import reverse
from django.conf import settings


# Create your models here.
class Championship(models.Model):

    # General
    name        = models.CharField("Naziv", max_length=64)
    club_count  = models.IntegerField(
        "Ukupan broj klubova", null=True, blank=True)
    club_position = models.IntegerField(
        "Pozicija kluba", null=True, blank=True)
    description = models.TextField("Opis", null=True, blank=True)
    location    = models.CharField("Lokacija", max_length=96)
    image       = models.ImageField("Slika", null=True, upload_to='champtionships/images/')

    # Date & Time
    start_date  = models.DateField("Datum početka")
    end_date    = models.DateField("Datum završetka")

    # Foreign keys
    city        = models.ForeignKey(
        "events.City", on_delete=models.CASCADE)
    organizer   = models.ForeignKey(
        "championships.Organizer", on_delete=models.CASCADE)
    gallery     = models.ForeignKey(
        "gallery.Gallery", null=True, blank=True, on_delete=models.SET_NULL)
    championship_type = models.ForeignKey(
        "championships.ChampionshipType", on_delete=models.CASCADE)

    class Meta:
        ordering = ['-start_date']
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


class ChampionshipType(models.Model):
    CHAMPIONSHIP_TYPE_CHOICES = (
        (1, 'Prvenstvo Hrvatske'),
        (2, 'Prvenstvo Centralne Europske Zone'),
        (3, 'Adria Drift Series'),
        (4, 'Day of Champions'),
        (5, 'FIA Hill CLimb Masters'),
        (6, 'Formula Driver'),
        (7, 'Auto i karting liga Zapad'),
        (8, 'Auto i karting savez Istre'),
    )

    name = models.CharField("Naziv", max_length=128)

    class Meta:
        verbose_name = "Tip prvenstva"
        verbose_name_plural = "Tipovi prvenstava"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("championship:detail", kwargs={"pk": self.pk})


class Category(models.Model):
    CATEGORY_CHOICES = (
        (1, 'Brdo'),
        (2, 'Formula Driver'),
        (3, 'Drift'),
        (4, 'General'),
    )

    # General
    name = models.IntegerField(
        "Naziv kategorije", choices=CATEGORY_CHOICES, default=4)
    championship_type = models.ForeignKey(
        "championships.ChampionshipType", on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        verbose_name = "Kategorija"
        verbose_name_plural = "Kategorije"

    def __str__(self):
        return self.get_name_display()


class SubCategory(models.Model):

    # General
    name = models.CharField(
        "Naziv kategorije", default="General", max_length=64)
    category = models.ForeignKey(
        "championships.Category", on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        verbose_name = "Podkategorija"
        verbose_name_plural = "Podkategorije"
    
    def results(self, championship):
        return DriverSubCategoryPosition.objects.filter(subcategory=self, championship=championship)

    def __str__(self):
        return self.name


class DriverSubCategoryPosition(models.Model):

    # Rank
    position = models.IntegerField("Mjesto", null=True)

    # Foreign keys
    subcategory = models.ForeignKey(
        "championships.SubCategory", verbose_name="Podkategorija", on_delete=models.CASCADE)
    driver = models.ForeignKey(
        "drivers.Driver", verbose_name="Vozač", on_delete=models.CASCADE)
    championship = models.ForeignKey(
        "championships.Championship", on_delete=models.CASCADE)

    class Meta:
        ordering = ['position']
        unique_together = ['subcategory', 'driver']
        index_together = ['subcategory', 'driver']
        verbose_name = "Pozicija natjecatelja"
        verbose_name_plural = "Pozicije natjecatelja"


class Organizer(models.Model):

    name = models.CharField("Naziv", max_length=64)

    class Meta:
        verbose_name = "Organizator"
        verbose_name_plural = "Organizatori"

    def __str__(self):
        return self.name
