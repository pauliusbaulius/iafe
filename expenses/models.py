import datetime
import os
from uuid import uuid4

import pytz
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.deconstruct import deconstructible


class Location(models.Model):
    # TODO https://pypi.org/project/django-address/
    #  if google api is okay :^)

    # FIXME this is pretty bad, unless I would make enum which would need to be updated on trips ...
    COUNTRY = (
        ("LT", "Lithuania"),
        ("DE", "Germany"),
        ("US", "USA"),
        ("PL", "Poland"),
        ("FR", "France"),
    )

    TYPE = (("Online", "Online"), ("Physical", "Physical"), ("Both", "Both"))

    title = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=TYPE, default="PHYSICAL")
    street = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=2, choices=COUNTRY, default="LT")
    website = models.URLField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("location-detail", args=[str(self.id)])

    def __str__(self):
        return f"{self.title} {self.type}"


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


class Label(models.Model):
    label = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.label

    def get_absolute_url(self):
        return reverse("label-detail", args=[str(self.id)])



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
    TZ = (("UTC", "UTC"), ("Europe/Vilnius", "Europe/Vilnius"), ("Europe/Berlin", "Europe/Berlin"))

    date = models.DateField(db_index=True)
    time = models.TimeField(null=True, blank=True)
    datetime_utc = models.DateTimeField(null=True, blank=True, db_index=True)
    # TODO default should be last entry from db by the user!
    timezone = models.CharField(max_length=20, choices=TZ, default="Europe/Vilnius")
    amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Amount of € spent.")
    location = models.ForeignKey("Location", on_delete=models.SET_NULL, null=True)
    payment = models.ForeignKey("Payment", on_delete=models.SET_NULL, db_index=True, null=True)
    document = models.FileField(upload_to=UploadToPathAndRename("documents/"), blank=True, null=True)
    image = models.ImageField(upload_to=UploadToPathAndRename("images/"), blank=True, null=True)
    comment = models.TextField(null=True, blank=True, help_text="Additional notes...")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    labels = models.ManyToManyField(Label)

    def __str__(self):
        return f"[{self.date} {self.time}] [{self.amount}€] [{self.location.title}] [{self.labels.all()}]"

    def get_absolute_url(self):
        return reverse("expense-detail", args=[str(self.id)])

    def convert_to_utc(self):
        user_tz = pytz.timezone(self.timezone)  # Get timezone of user from input
        date = datetime.datetime(
            year=self.date.year, month=self.date.month, day=self.date.day, hour=self.time.hour, minute=self.time.minute
        )  # Ugliest way to create a datetime :^)
        date = user_tz.localize(date)  # Convert it to users time aka replace +00:00 to their tz.
        date = date.astimezone(pytz.utc)  # Convert cleaned and right datetime into utc.
        self.datetime_utc = date  # Store utc datetime in db together with our localized datetime.

    def save(self, *args, **kwargs):
        self.convert_to_utc()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-date", "-time"]
