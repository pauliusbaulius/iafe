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


class DateInput(forms.DateInput):
    input_type = "date"


class TimeInput(forms.TimeInput):
    input_type = "time"


class FileInput(forms.FileInput):
    input_type = "file"


class ExpenseCreateForm(forms.ModelForm):
    class Meta:
        model = Expense
        exclude = ["owner"]
        widgets = {"date": DateInput(), "time": TimeInput()}


class LocationCreateForm(forms.ModelForm):
    class Meta:
        model = Location
        exclude = ["owner"]


class PaymentCreateForm(forms.ModelForm):
    class Meta:
        model = Payment
        exclude = ["owner"]
