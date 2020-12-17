from django import forms
from expenses.models import Expense

class ExpenseCreateForm(forms.ModelForm):
    class Meta:
        model = Expense
        exclude = ["owner"]