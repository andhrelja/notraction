from django.db import models
from django.shortcuts import reverse


class Driver(models.Model):
    GENDER_CHOICES = (
        ('M', 'Muško'),
        ('Z', 'Žensko'),
        ('O', 'Ostalo')
    )

    DISCIPLINE_CHOICES = (
        (1, 'Brdo'),
        (2, 'Formula Driver'),
        (3, 'Drift'),
    )

    # General
    first_name      = models.CharField("Ime", max_length=64)
    last_name       = models.CharField("Prezime", max_length=64)
    birth_date      = models.DateField("Datum rođenja")
    gender          = models.CharField("Spol", max_length=1, default='M', choices=GENDER_CHOICES)
    driver_image    = models.ImageField("Slika", default='accounts/profile/default.jpg', upload_to='people/images/')

    # Contact
    email           = models.EmailField("Email")
    phone           = models.CharField("Telefon", max_length=15)

    # Foreign keys
    city            = models.ForeignKey("events.City", verbose_name="Grad", on_delete=models.CASCADE)
    discipline      = models.IntegerField("Disciplina", choices=DISCIPLINE_CHOICES, default=2)
    

    @property
    def location_name(self):
        location_name = "{city}, {county}".format(city=self.city, county=self.city.county)
        return location_name.strip()

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
