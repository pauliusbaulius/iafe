from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, FormView,
                                  ListView, UpdateView)

from expenses.forms import (ExpenseCreateForm, LabelCreateForm,
                            LocationCreateForm, PaymentCreateForm)
from expenses.models import Expense, Label, Location, Payment


class ExpenseListView(LoginRequiredMixin, ListView):
    model = Expense
    context_object_name = "my_expense_list"
    template_name = "expenses/index.html"
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
    success_url = reverse_lazy("expenses-index")

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
    success_url = reverse_lazy("expenses-index")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = Expense
    context_object_name = "item"
    template_name = "expenses/generic_delete.html"
    success_url = reverse_lazy("expenses-index")


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


class LabelDetailView(LoginRequiredMixin, DeleteView):
    model = Label
    context_object_name = "item"
    template_name = "expenses/generic_detail.html"


class LabelCreateView(LoginRequiredMixin, CreateView):
    model = Label
    form_class = LabelCreateForm
    template_name = "expenses/generic_form.html"
    success_url = reverse_lazy("label-list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(LabelCreateView, self).form_valid(form)


class LabelUpdateView(LoginRequiredMixin, UpdateView):
    model = Label
    form_class = LabelCreateForm
    template_name = "expenses/generic_form.html"
    success_url = reverse_lazy("label-list")


class LabelDeleteView(LoginRequiredMixin, DeleteView):
    model = Label
    context_object_name = "item"
    template_name = "expenses/generic_delete.html"
    success_url = reverse_lazy("label-list")


class LabelListView(LoginRequiredMixin, ListView):
    model = Label
    context_object_name = "label_list"
    template_name = "expenses/label_list.html"
    paginate_by = 100

    def get_queryset(self):
        return Label.objects.filter(owner=self.request.user).all()
