from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.templatetags.static import static

from drivers.models import CarDriver

from PIL import Image
from io import BytesIO
import requests
import os

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
    horse_power = models.IntegerField("Konjska snaga", null=True, blank=True)
    capacity = models.IntegerField(
        "Kubikaža", choices=CAPACITY_CHOICES, null=True)
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
        return car_driver.active

    def get_full_name(self):
        full_name = "{make} {model}, {year}".format(
            make=self.model.manufacturer, model=self.model, year=self.year)
        return full_name.strip()
    
    def get_short_name(self):
        short_name = "{model}, {year}".format(model=self.model, year=self.year)
        return short_name.strip()

    def get_driver(self):
        car_driver = CarDriver.objects.filter(car=self, active=True)
        if not car_driver.exists():
            car_driver = CarDriver.objects.filter(car=self)
        return car_driver.first()
        

    # TODO: Crop driver image to a square

    def __str__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return reverse("cars:detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Automobil"
        verbose_name_plural = "Automobili"


class Manufacturer(models.Model):

    # General
    name = models.CharField("Naziv", max_length=128)
    image_url = models.CharField("Logo URL", max_length=2000)

    class Meta:
        verbose_name = "Proizvođač"
        verbose_name_plural = "Proizvođači"

    @property
    def image_thumbnail_url(self):
        file_name = os.path.split(self.image_url)[1]
        img_path = settings.BASE_DIR / 'static/images/manufacturer_logos' / file_name

        try:
            open(img_path)
        except FileNotFoundError:
            response = requests.get(self.image_url)
            buff = BytesIO(response.content)       

            img = Image.open(buff)            
            img = img.convert("RGBA")
            img = img.reduce(12)
            
            img_array = img.getdata()
            new_img_array = []
            for item in img_array:
                if item[0] == 255 and item[1] == 255 and item[2] == 255:
                    new_img_array.append((255, 255, 255, 0))
                else:
                    new_img_array.append(item)

            img.putdata(new_img_array)
            with open(img_path, 'wb') as f:
                img.save(f, "PNG")

        return static('images/manufacturer_logos/' + file_name)

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
