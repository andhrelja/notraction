from django.db import models, reset_queries
from django.shortcuts import reverse


class Driver(models.Model):
    GENDER_CHOICES = (
        ('M', 'Muško'),
        ('Z', 'Žensko'),
        ('O', 'Ostalo')
    )

    # General
    first_name      = models.CharField("Ime", max_length=64)
    last_name       = models.CharField("Prezime", max_length=64)
    birth_date      = models.DateField("Datum rođenja")
    gender          = models.CharField("Spol", max_length=1, default='M', choices=GENDER_CHOICES)
    driver_image    = models.ImageField( # , width_field='512', height_field='512'
        "Slika", default='accounts/profile/default.jpg', upload_to='people/images/')

    # Contact
    email           = models.EmailField("Email")
    phone           = models.CharField("Telefon", max_length=15)

    # Foreign keys
    city            = models.ForeignKey("events.City", verbose_name="Grad", on_delete=models.CASCADE)
    categories      = models.ManyToManyField("championships.Category", verbose_name="Discipline natjecanja")
    

    @property
    def location_name(self):
        location_name = "{city}, {county}".format(city=self.city, county=self.city.county)
        return location_name.strip()
    
    @property
    def championships(self):
        subcategory_positions = self.driversubcategoryposition_set.all()
        return set([result.championship for result in subcategory_positions.select_related('championship')])
    
    @property
    def get_categories_display(self):
        categories = (cat.get_name_display() for cat in self.categories.all())
        return ", ".join(categories)

    def get_active_car(self):
        cars = self.cars(active=True)
        if len(cars) == 1:
            return cars[0]
        return None

    def cars(self, active=False):
        if active:
            cars = (cd.car for cd in self.cardriver_set.filter(driver=self, active=True))
        else:
            cars = (cd.car for cd in self.cardriver_set.filter(driver=self))
        return list(cars)

    def get_full_name(self):
        full_name = '{first} {last}'.format(first=self.first_name, last=self.last_name)
        return full_name.strip()

    def __str__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return reverse("drivers:detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Vozač"
        verbose_name_plural = "Vozači"        


class DriverSubCategoryPosition(models.Model):
    CHAMPIONSHIP_TYPE_CHOICES = (
        ('ph', 'PH'),
        ('pir', 'PIR')
    )

    # Rank
    position = models.IntegerField("Mjesto", null=True)
    championship_type = models.CharField("Prvenstvo", choices=CHAMPIONSHIP_TYPE_CHOICES, max_length=32)

    # Foreign keys
    subcategory = models.ForeignKey(
        "championships.SubCategory", verbose_name="Podkategorija", on_delete=models.CASCADE)
    driver = models.ForeignKey(
        "drivers.Driver", verbose_name="Vozač", on_delete=models.CASCADE)
    championship = models.ForeignKey(
        "championships.Championship", on_delete=models.CASCADE)

    class Meta:
        ordering = ['position']
        unique_together = ['championship', 'subcategory', 'driver']
        index_together = ['championship', 'subcategory', 'driver']
        verbose_name = "Pozicija natjecatelja"
        verbose_name_plural = "Pozicije natjecatelja"


class CarDriver(models.Model):

    car    = models.ForeignKey("cars.Car", verbose_name="Automobil", on_delete=models.CASCADE)
    driver = models.ForeignKey("drivers.Driver", verbose_name="Vozač", on_delete=models.CASCADE)
    active = models.BooleanField("Aktivan", default=True)
    date_deactivated = models.DateTimeField("Datum deaktivacije", auto_now=False, auto_now_add=False, null=True)

    class Meta:
        verbose_name = "Vozač automobila"
        verbose_name_plural = "Vozači automobila"
        unique_together = ['car', 'active']
    
    def __str__(self):
        return self.driver.get_full_name()