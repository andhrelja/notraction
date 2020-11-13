from django.db import models
from django.shortcuts import reverse
from django.conf import settings


# Create your models here.
class Championship(models.Model):

    # General
    name        = models.CharField("Naziv", max_length=64)
    clubs_count = models.IntegerField("Ukupan broj klubova")
    club_position = models.IntegerField("Pozicija kluba")

    # Date & Time
    start_date  = models.DateField("Datum početka")
    end_date    = models.DateField("Datum završetka")

    # Foreign keys
    city        = models.ForeignKey("events.City", verbose_name="Grad", on_delete=models.CASCADE)
    gallery     = models.ForeignKey("gallery.Gallery", verbose_name="Galerija",
                                    null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['-start_date']
        verbose_name = "Prvenstvo"
        verbose_name_plural = "Prvenstva"
    

    @property
    def location_name(self):
        location_name = "{city}, {county}".format(city=self.city, county=self.city.county)
        return location_name.strip()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("championships:detail", kwargs={"pk": self.pk})


class Category(models.Model):
    CATEGORY_CHOICES = (
        (1, 'Brdo'),
        (2, 'Formula Driver'),
        (3, 'Drift'),
        (4, 'General'),
    )

    # General
    name         = models.IntegerField("Naziv kategorije", choices=CATEGORY_CHOICES, default=4)
    championship = models.ForeignKey("championships.Championship", verbose_name="Prvenstvo", on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        verbose_name = "Kategorija"
        verbose_name_plural = "Kategorije"

    def __str__(self):
        return self.name


class SubCategory(models.Model):

    # General
    name         = models.CharField("Naziv kategorije", default="General", max_length=64)
    category     = models.ForeignKey("championships.Category", verbose_name="Podkategorija", on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        verbose_name = "Podkategorija"
        verbose_name_plural = "Podkategorije"

    def __str__(self):
        return self.name


class CategoryDriverPosition(models.Model):

    # Rank
    position    = models.IntegerField("Mjesto", null=True)

    # Foreign keys
    subcategory = models.ForeignKey("championships.SubCategory", verbose_name="Podkategorija", on_delete=models.CASCADE)
    driver      = models.ForeignKey("drivers.Driver", verbose_name="Vozač", on_delete=models.CASCADE)

    class Meta:
        ordering = ['position']
        unique_together = ['subcategory', 'driver']
        index_together = ['subcategory', 'driver']
        verbose_name = "Pozicija natjecatelja"
        verbose_name_plural = "Pozicije natjecatelja"
