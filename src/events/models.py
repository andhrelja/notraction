from django.utils import timezone
from django.db import models
from django.shortcuts import reverse
from datetime import datetime


class Event(models.Model):

    # General
    name        = models.CharField("Naziv", max_length=64)
    cover       = models.ImageField("Slika", upload_to='events/images/')
    description = models.TextField("Opis")

    # Date & Time
    start_date = models.DateField("Datum početka")
    end_date   = models.DateField("Datum završetka")

    start_time = models.TimeField("Vrijeme početka")
    end_time   = models.TimeField("Vrijeme završetka")

    # Foreign keys
    city        = models.ForeignKey("events.City", verbose_name="Grad", on_delete=models.CASCADE)
    author      = models.ForeignKey("auth.User", verbose_name="Autor", related_name="author", on_delete=models.CASCADE)
    album       = models.ManyToManyField("gallery.Gallery", verbose_name="Galerija")

    class Meta:
        verbose_name = "Događaj"
        verbose_name_plural = "Događaji"
        ordering = ["-start_date"]


    @property
    def location_name(self):
        location_name = "{city}, {county}".format(city=self.city, county=self.city.county)
        return location_name.strip()

    @property
    def timedelta_name(self):
        now = timezone.now()
        event_datetime = datetime.combine(self.start_date, self.start_time)
        time_delta = timezone.make_aware(event_datetime) - now
        seconds = time_delta.seconds
        
        periods = [
            ('godina',  60*60*24*365),
            ('mjeseca', 60*60*24*30),
            ('dana',    60*60*24),
            ('sati',    60*60)
        ]

        strings=[]
        for period_name, period_seconds in periods:
            if seconds > period_seconds:
                period_value , seconds = divmod(seconds, period_seconds)
                strings.append("%s %s" % (period_value, period_name))

        return ", ".join(strings)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("events:detail", kwargs={"pk": self.pk})


class County(models.Model):

    # General
    id      = models.IntegerField("ID", primary_key=True)
    name    = models.CharField("Naziv", max_length=64)

    class Meta:
        verbose_name = "Županija"
        verbose_name_plural = "Županije"

    def __str__(self):
        return self.name


class City(models.Model):
    TYPE_CHOICES = (
        (1, 'Grad'),
        (2, 'Općina'),
    )

    # General
    name        = models.CharField("Naziv", max_length=64)
    full_name   = models.CharField("Puni naziv", max_length=128)
    city_type   = models.IntegerField("Tip mjesta", choices=TYPE_CHOICES)

    # Foreign keys
    county      = models.ForeignKey("events.County", verbose_name="Županija", on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Grad"
        verbose_name_plural = "Gradovi"

    def __str__(self):
        return self.full_name

# TODO: Create Countries