from django.db import models
from django.urls import reverse
import os

def get_upload_path(image_instance, filename):
    return os.path.join('gallery', 'images', filename)


class Gallery(models.Model):

    # General
    name    = models.CharField("Naziv", max_length=64)

    # Foreign keys
    images  = models.ManyToManyField("gallery.Image", blank=True, verbose_name="Slike")

    @property
    def championship(self):
        championship = self.championship_set.first()
        return championship
    
    def display_name(self):
        display_name = self.championship.name + " - " + self.name
        return display_name.strip()

    class Meta:
        verbose_name = "Galerija"
        verbose_name_plural = "Galerije"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("gallery:detail", kwargs={"pk": self.pk})
    


class Image(models.Model):

    # General
    image   = models.ImageField("Slika", upload_to=get_upload_path, height_field=None, width_field=None, max_length=None)
    alt     = models.CharField("Naziv", max_length=50)
    drivers = models.ManyToManyField("drivers.Driver", verbose_name="Vozači na slici")

    class Meta:
        verbose_name = "Slika"
        verbose_name_plural = "Slike"

    def __str__(self):
        return self.alt
