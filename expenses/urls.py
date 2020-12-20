from django.urls import path

from . import views

urlpatterns = [
    ##path("", views.index, name="expenses-index"),
    path("", views.ExpenseListView.as_view(), name="expenses-index"),
    path("expense/<int:pk>", views.ExpenseDetailView.as_view(), name="expense-detail"),
    path("expense/create", views.ExpenseCreateView.as_view(), name="expense-create"),
    path("expense/<int:pk>/update", views.ExpenseUpdateView.as_view(), name="expense-update"),
    path("expense/<int:pk>/delete", views.ExpenseDeleteView.as_view(), name="expense-delete"),
    path("location/all", views.LocationListView.as_view(), name="location-list"),
    path("location/<int:pk>", views.LocationDetailView.as_view(), name="location-detail"),
    path("location/create", views.LocationCreateView.as_view(), name="location-create"),
    path("location/<int:pk>/update", views.LocationUpdateView.as_view(), name="location-update"),
    path("location/<int:pk>/delete", views.LocationDeleteView.as_view(), name="location-delete"),
    path("payment/all", views.PaymentListView.as_view(), name="payment-list"),
    path("payment/<int:pk>", views.PaymentDetailView.as_view(), name="payment-detail"),
    path("payment/create", views.PaymentCreateView.as_view(), name="payment-create"),
    path("payment/<int:pk>/update", views.PaymentUpdateView.as_view(), name="payment-update"),
    path("payment/<int:pk>/delete", views.PaymentDeleteView.as_view(), name="payment-delete"),
]
