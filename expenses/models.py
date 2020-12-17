import os
from uuid import uuid4

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from expenses.utils import path_and_rename


class Location(models.Model):
    # TODO https://pypi.org/project/django-address/
    #  if google api is okay :^)
    title = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    # FIXME this is pretty bad, unless I would make enum which would need to be updated on trips ...
    COUNTRY = (
        ("LT", "Lithuania"),
        ("DE", "Germany"),
    )
    country = models.CharField(max_length=2, choices=COUNTRY, default="LT")

    website = models.URLField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("location-detail", args=[str(self.id)])

    def __str__(self):
        return f"{self.title} [{self.street} - {self.city}, {self.country}]"


class Payment(models.Model):
    title = models.CharField(max_length=100)
    comment = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("payment-detail", args=[str(self.id)])

    def __str__(self):
        return f"{self.title}"


# class Document(models.Model):
#     document = models.FileField(upload_to="data/documents/")
#     expense = models.ForeignKey("Expense", on_delete=models.SET_NULL, null=True)
#
#
# class Picture(models.Model):
#     image = models.ImageField(upload_to="data/images/")
#     expense = models.ForeignKey("Expense", on_delete=models.SET_NULL, null=True)

from django.utils.deconstruct import deconstructible


@deconstructible
class UploadToPathAndRename(object):
    def __init__(self, path):
        self.sub_path = path

    def __call__(self, instance, filename):
        ext = filename.split(".")[-1]
        # get filename
        if instance.pk:
            filename = "{}.{}".format(instance.pk, ext)
        else:
            filename = "{}.{}".format(uuid4().hex, ext)
        return os.path.join(self.sub_path, filename)


class Expense(models.Model):
    date = models.DateField(db_index=True)
    time = models.TimeField(null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Amount of € spent.")
    location = models.ForeignKey("Location", on_delete=models.SET_NULL, null=True)
    document = models.FileField(
        upload_to=UploadToPathAndRename("documents/"), blank=True, null=True
    )
    image = models.ImageField(
        upload_to=UploadToPathAndRename("images/"), blank=True, null=True
    )
    payment = models.ForeignKey("Payment", on_delete=models.SET_NULL, db_index=True, null=True)
    comment = models.TextField(null=True, blank=True, help_text="Additional notes...")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"[{self.date} {self.time}] {self.amount}€"

    def get_absolute_url(self):
        return reverse("expense-detail", args=[str(self.id)])

    class Meta:
        ordering = ["-date", "-time"]
