from django.db import models
from django.shortcuts import reverse
from django.conf import settings


# Create your models here.
class Championship(models.Model):

    # General
    name = models.CharField("Naziv", max_length=64)
    level = models.CharField("Razina", max_length=64)  # extra

    # Date & Time
    start_date = models.DateField("Datum početka")
    end_date = models.DateField("Datum završetka")

    # Foreign keys
    city = models.ForeignKey("events.City", verbose_name="Grad", on_delete=models.CASCADE)
    discipline = models.ForeignKey("championships.Discipline", verbose_name="Disciplina",
                                   related_name="Disciplina", on_delete=models.CASCADE)
    gallery = models.ForeignKey("gallery.Gallery", verbose_name="Galerija",
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


class Discipline(models.Model):
    DISCIPLINE_CHOICES = (
        (1, 'Brdo'),
        (2, 'Formula Driver'),
        (3, 'Drift'),
    )

    # General
    id = models.AutoField(primary_key=True)
    name = models.CharField("Naziv", max_length=64)

    def create(self):
        discipline_objs = Discipline.objects.all()
        disciplines_count = len(self.DISCIPLINE_CHOICES)

        if disciplines_count != discipline_objs.count():
            for id, name in self.DISCIPLINE_CHOICES:
                discipline = Discipline.objects.create(id=id, name=name)
                if settings.DEBUG:
                    print("[INFO] Discipline {} created successfully".format(discipline))

    class Meta:
        ordering = ['name']
        verbose_name = "Disciplina"
        verbose_name_plural = "Discipline"

    def __str__(self):
        return self.name


class Category(models.Model):

    # General
    name = models.CharField("Naziv kategorije", default="General", max_length=64)
    championship = models.ForeignKey("championships.Championship", verbose_name="Prvenstvo", on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        verbose_name = "Kategorija"
        verbose_name_plural = "Kategorije"

    def __str__(self):
        return self.name


class CategoryDriverPosition(models.Model):

    # Rank
    position = models.IntegerField("Mjesto", null=True)

    # Foreign keys
    category = models.ForeignKey("championships.Category", verbose_name="Kategorija", on_delete=models.CASCADE)
    driver = models.ForeignKey("drivers.Driver", verbose_name="Vozač", on_delete=models.CASCADE)

    class Meta:
        ordering = ['position']
        unique_together = ['category', 'driver']
        index_together = ['category', 'driver']
        verbose_name = "Pozicija natjecatelja"
        verbose_name_plural = "Pozicije natjecatelja"
