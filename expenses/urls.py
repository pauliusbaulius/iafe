from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="expenses-index"),
    path("expense/all", views.ExpenseListView.as_view(), name="expense-list"),
    path("expense/<int:pk>", views.ExpenseDetailView.as_view(), name="expense-detail"),
    path("expense/create", views.ExpenseCreateView.as_view(), name="expense-create"),
    path("expense/<int:pk>/update", views.ExpenseUpdateView.as_view(), name="expense-update"),
    path("expense/<int:pk>/delete", views.ExpenseDeleteView.as_view(), name="expense-delete"),
]
