from django.conf import settings
from django.db import models
from django.shortcuts import reverse

from drivers.models import CarDriver


YEAR_CHOICES = (
    ((x, x) for x in range(2019, 1950, -1))
)


class Car(models.Model):

    # General
    horse_power = models.IntegerField("Konjska snaga", null=True, blank=True)
    capacity = models.CharField("Kubikaža", max_length=3, null=False, blank=False)
    year = models.IntegerField("Godina proizvodnje", choices=YEAR_CHOICES)
    description = models.TextField("Detalji", null=True, blank=True)

    # Foreign keys
    model = models.ForeignKey(
        "cars.Model", verbose_name="Model", on_delete=models.CASCADE)

    # Images
    image = models.ImageField(
        "Slika", upload_to='cars/images/', blank=False, null=True)
    albums = models.ManyToManyField("gallery.Gallery", verbose_name="Albumi")

    @property
    def is_active(self):
        car_driver = self.cardriver_set.first()
        if car_driver:
            return car_driver.active
        return False
    

    def get_full_name(self):
        full_name = "{make} {model}".format(
            make=self.model.manufacturer, model=self.model)
        return full_name.strip()
    
    def get_short_name(self):
        short_name = "{model}, {year}".format(model=self.model, year=self.year)
        return short_name.strip()

    def get_driver(self):
        car_driver = CarDriver.objects.filter(car=self, active=True)
        if not car_driver.exists():
            car_driver = CarDriver.objects.filter(car=self)
        car_driver = car_driver.first()
        return car_driver.driver
        

    # TODO: Crop driver image to a square

    def __str__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return reverse("cars:detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Automobil"
        verbose_name_plural = "Automobili"
        ordering = ['model__manufacturer__name']


class Manufacturer(models.Model):

    # General
    name = models.CharField("Naziv", max_length=128)
    image_url = models.CharField("Logo URL", max_length=2000)

    class Meta:
        verbose_name = "Proizvođač"
        verbose_name_plural = "Proizvođači"

    @property
    def image_thumbnail_url(self):
        return self.image_url

    def __str__(self):
        return self.name


class Model(models.Model):

    # General
    name = models.CharField("Naziv", max_length=50)

    # Foreign keys
    manufacturer = models.ForeignKey(
        "cars.Manufacturer", verbose_name="Proizvođač", on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        verbose_name = "Model automobila"
        verbose_name_plural = "Modeli automobila"


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("cars:list")
