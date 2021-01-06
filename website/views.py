from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render

from expenses.models import Expense


@login_required
def index(request):
    ammount_expenses = Expense.objects.filter(owner=request.user).count()
    total_spent = "{:.2f}".format(
        Expense.objects.filter(owner=request.user).aggregate(Sum("amount"))[
            "amount__sum"
        ]
    )
    context = {"expenses": ammount_expenses, "total_spent": total_spent}
    return render(request, "index.html", context=context)
