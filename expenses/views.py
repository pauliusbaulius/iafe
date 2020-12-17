from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView, UpdateView, CreateView

from expenses.models import Expense
from expenses.forms import ExpenseCreateForm


@login_required
def index(request):
    context = {}
    return render(request, "expenses/index.html", context=context)


class ExpenseListView(LoginRequiredMixin, ListView):
    model = Expense
    context_object_name = "my_expense_list"
    template_name = "expenses/expense_list.html"
    paginate_by = 100

    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user).all()


class ExpenseDetailView(LoginRequiredMixin, DetailView):
    model = Expense
    template_name = "expenses/expense_detail.html"


class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    form_class = ExpenseCreateForm
    template_name = "expenses/expense_form.html"
    #fields = ["date", "time", "amount", "location", "payment", "comment"]

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(ExpenseCreateView, self).form_valid(form)


class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    model = Expense
    template_name = "expenses/expense_form.html"


class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = Expense
    success_url = reverse_lazy("expenses")