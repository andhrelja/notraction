from django.db import models
import os

def get_upload_path(image_instance, filename):
    return os.path.join(image_instance.app_name, 'images', filename)


class Gallery(models.Model):

    # General
    name    = models.CharField("Naziv", max_length=64)

    # Foreign keys
    images  = models.ManyToManyField("gallery.Image", verbose_name="Slike")

    class Meta:
        verbose_name = "Galerija"
        verbose_name_plural = "Galerije"

    def __str__(self):
        return self.name


class Image(models.Model):

    # General
    image   = models.ImageField("Slika", upload_to=get_upload_path, height_field=None, width_field=None, max_length=None)
    alt     = models.CharField("Naziv", max_length=50)

    class Meta:
        # app_label = str()
        verbose_name = "Slika"
        verbose_name_plural = "Slike"

    def __str__(self):
        return self.alt
