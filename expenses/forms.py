from datetime import datetime

from django import forms
from django.contrib.admin import widgets
from django.forms import DateInput, DateTimeField, MultiWidget, TextInput

from expenses.models import Expense, Location, Payment

"""
For some reason Django is not smart enough to use HTML input types itself,
so you need to create classes like below and pass them as widgets!

https://www.w3schools.com/html/html_form_input_types.asp
https://stackoverflow.com/questions/3367091/whats-the-cleanest-simplest-to-get-running-datepicker-in-django/35968816#35968816

"""


class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"


class DateInput(forms.DateInput):
    input_type = "date"


class TimeInput(forms.TimeInput):
    input_type = "time"


class FileInput(forms.FileInput):
    input_type = "file"


class ExpenseCreateForm(forms.ModelForm):
    class Meta:
        model = Expense
        exclude = (
            "owner",
            "datetime_utc",
        )
        widgets = {"date": DateInput(), "time": TimeInput()}
        # widgets = {"datetime": DateTimeInput()}

    def __init__(self, *args, user, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["location"].queryset = user.location_set.all()
        self.fields["payment"].queryset = user.payment_set.all()


class LocationCreateForm(forms.ModelForm):
    class Meta:
        model = Location
        exclude = ["owner"]


class PaymentCreateForm(forms.ModelForm):
    class Meta:
        model = Payment
        exclude = ["owner"]
