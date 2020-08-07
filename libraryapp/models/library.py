from django.db import models
from django.urls import reverse

class Library(models.Model):

    title = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = ("Library")
        verbose_name_plural = ("libraries")

    def get_absolute_url(self):
        return reverse("library_details", kwargs={"pk": self.pk})
