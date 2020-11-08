from django.db import models
from django.shortcuts import reverse
from django.conf import settings

from pathlib import Path
import json

CAPACITY_CHOICES = (
    (0, 1000),
    (1, 1200),
    (2, 1400),
    (3, 1600),
    (4, 1800),
    (5, 1900),
    (6, 2000),
    (7, 2200),
    (8, 2400),
    (9, 3000),
)

YEAR_CHOICES = (
    ((x, x) for x in range(2019, 1950, -1))
)


class Car(models.Model):       
    
    # General
    horse_power = models.IntegerField("Konjske snage", null=True, blank=True)
    capacity    = models.IntegerField("Kubikaža", choices=CAPACITY_CHOICES, null=True)
    year        = models.IntegerField("Godina proizvodnje", choices=YEAR_CHOICES)
    description = models.TextField("Detalji", null=True, blank=True)

    # Foreign keys
    driver      = models.ForeignKey("drivers.Driver", verbose_name="Vozač", on_delete=models.CASCADE)
    model       = models.ForeignKey("cars.Model", verbose_name="Model", on_delete=models.CASCADE)

    # Images
    image       = models.ImageField("Slika", upload_to='cars/images/', blank=False, null=True)
    gallery     = models.ForeignKey("gallery.Gallery", null=True, blank=True, verbose_name="Galerija", on_delete=models.CASCADE)
    

    def get_full_name(self):
        full_name = "{model}, {year}".format(model=self.model, year=self.year)
        return full_name.strip()

    def __str__(self):
        return "{make} {model}, {year}".format(self.make, self.model, self.year)
    
    def get_absolute_url(self):
        return reverse("cars:detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Automobil"
        verbose_name_plural = "Automobili"


class Manufacturer(models.Model):

    # General
    name    = models.CharField("Naziv", max_length=128)

    class Meta:
        verbose_name = "Proizvođač"
        verbose_name_plural = "Proizvođači"

    def __str__(self):
        return self.name


class Model(models.Model):

    # General
    name    = models.CharField("Naziv", max_length=50)

    # Foreign keys
    manufacturer = models.ForeignKey("cars.Manufacturer", verbose_name="Proizvođač", on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        verbose_name = "Model automobila"
        verbose_name_plural = "Modeli automobila"

    def load_data(self, reload=True):
        if reload:
            Model.objects.all().delete()
        
        dictionary = get_json_content('proizvodjaci_modeli.json')
        for manufacturer in dictionary:
            make_id = manufacturer['id'] + 1
            make = Manufacturer.objects.create(id=make_id, name=manufacturer['name'])
            for model in manufacturer['brands']:
                model_id = model['id'] + 1
                Model.objects.create(
                    id=model_id,
                    name=model['name'],
                    manufacturer=make)
            if settings.DEBUG:
                print("[INFO] Proizvodjac {} s pripadajućim "
                    "gradovima uspješno stvorena".format(make))                    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("cars:list")


def get_json_content(filename):
    static_root = Path(settings.STATIC_ROOT).resolve()
    with open(static_root / 'input_data' / filename, 'r') as f:
        json_content = json.load(f)
    return json_content
