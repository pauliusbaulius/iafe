from datetime import datetime

from django import forms
from django.contrib.admin import widgets
from django.forms import DateInput, DateTimeField, MultiWidget, TextInput

from expenses.models import Expense

"""
For some reason Django is not smart enough to use HTML input types itself,
so you need to create classes like below and pass them as widgets!
"""


class DateInput(forms.DateInput):
    input_type = "date"


class TimeInput(forms.TimeInput):
    input_type = "time"


class ExpenseCreateForm(forms.ModelForm):
    class Meta:
        model = Expense
        exclude = ["owner"]
        widgets = {"date": DateInput(), "time": TimeInput()}
