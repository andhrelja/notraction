from django.shortcuts import reverse
from django.db import models


class Profile(models.Model):

    # General
    user          = models.OneToOneField("auth.User", verbose_name="Korisnik", on_delete=models.CASCADE)
    profile_image = models.ImageField("Slika", upload_to='accounts/images/', default="accounts/images/default.jpg", max_length=255)

    class Meta:
        verbose_name = 'Profil'
        verbose_name_plural = 'Profili'

    def __str__(self):
        full_name = '{first} {last}'.format(first=self.user.first_name, last=self.user.last_name)
        return full_name.strip()

    def get_absolute_url(self):
        return reverse("accounts:detail", kwargs={"pk": self.pk})
