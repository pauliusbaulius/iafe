from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render

from expenses.models import Expense


@login_required
def index(request):
    amount_expenses = Expense.objects.filter(owner=request.user).count()
    total_amount = Expense.objects.filter(owner=request.user).aggregate(Sum("amount"))[
        "amount__sum"
    ]
    total_spent = "{:.2f}".format(total_amount if total_amount else 0)
    context = {"expenses": amount_expenses, "total_spent": total_spent}
    return render(request, "index.html", context=context)
