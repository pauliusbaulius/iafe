from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, FormView,
                                  ListView, UpdateView)

from expenses.forms import (ExpenseCreateForm, LocationCreateForm,
                            PaymentCreateForm)
from expenses.models import Expense, Location, Payment


@login_required
def index(request):
    context = {}
    return render(request, "expenses/index.html", context=context)


class ExpenseListView(LoginRequiredMixin, ListView):
    model = Expense
    context_object_name = "my_expense_list"
    template_name = "expenses/expense_list.html"
    paginate_by = 100

    # TODO extra_context = .. for static
    #  https://www.valentinog.com/blog/get-context-data/ for dynamic!
    #  from filters.py to have filtered table
    #  https://django-tables2.readthedocs.io/en/latest/pages/filtering.html#filtering

    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user).all()


class ExpenseDetailView(LoginRequiredMixin, DetailView):
    model = Expense
    template_name = "expenses/expense_detail.html"


class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    form_class = ExpenseCreateForm
    template_name = "expenses/expense_form.html"
    success_url = reverse_lazy("expense-list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(ExpenseCreateView, self).form_valid(form)


class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    model = Expense
    form_class = ExpenseCreateForm
    template_name = "expenses/expense_form.html"
    success_url = reverse_lazy("expense-list")


class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = Expense
    template_name = "expenses/expense_delete.html"
    success_url = reverse_lazy("expense-list")


class LocationListView(LoginRequiredMixin, ListView):
    model = Location
    context_object_name = "location_list"
    template_name = "expenses/location_list.html"
    paginate_by = 100

    def get_queryset(self):
        return Location.objects.filter(owner=self.request.user).all()


class LocationDetailView(LoginRequiredMixin, DeleteView):
    model = Location
    context_object_name = "item"
    template_name = "expenses/generic_detail.html"


class LocationCreateView(LoginRequiredMixin, CreateView):
    model = Location
    form_class = LocationCreateForm
    template_name = "expenses/generic_form.html"
    success_url = reverse_lazy("location-list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(LocationCreateView, self).form_valid(form)


class LocationUpdateView(LoginRequiredMixin, UpdateView):
    model = Location
    form_class = LocationCreateForm
    template_name = "expenses/generic_form.html"
    success_url = reverse_lazy("location-list")


class LocationDeleteView(LoginRequiredMixin, DeleteView):
    model = Location
    context_object_name = "item"
    template_name = "expenses/generic_delete.html"
    success_url = reverse_lazy("location-list")


class PaymentListView(LoginRequiredMixin, ListView):
    model = Payment
    context_object_name = "payment_list"
    template_name = "expenses/payment_list.html"
    paginate_by = 100

    def get_queryset(self):
        return Payment.objects.filter(owner=self.request.user).all()


class PaymentDetailView(LoginRequiredMixin, DeleteView):
    model = Payment
    context_object_name = "item"
    template_name = "expenses/generic_detail.html"


class PaymentCreateView(LoginRequiredMixin, CreateView):
    model = Payment
    form_class = PaymentCreateForm
    template_name = "expenses/generic_form.html"
    success_url = reverse_lazy("payment-list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PaymentCreateView, self).form_valid(form)


class PaymentUpdateView(LoginRequiredMixin, UpdateView):
    model = Payment
    form_class = PaymentCreateForm
    template_name = "expenses/generic_form.html"
    success_url = reverse_lazy("payment-list")


class PaymentDeleteView(LoginRequiredMixin, DeleteView):
    model = Payment
    context_object_name = "item"
    template_name = "expenses/generic_delete.html"
    success_url = reverse_lazy("payment-list")
