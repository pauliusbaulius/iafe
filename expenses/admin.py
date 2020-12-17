from django.contrib import admin

from .models import Document, Expense, Location, Payment, Picture


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("title", "street", "city", "country", "owner")


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("title", "owner")


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):

    list_display = ("date", "time", "amount", "location", "payment", "owner")
    list_filter = ("date", "amount", "location", "payment", "owner")

    fieldsets = (
        (None, {"fields": (("date", "time"), "amount", "location", "payment", "owner")}),
        ("Miscellaneous", {"fields": ("comment",)}),
    )


admin.site.register(Document)
admin.site.register(Picture)
