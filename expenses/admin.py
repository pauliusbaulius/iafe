from django.contrib import admin

from .models import Expense, Location, Payment


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("title", "street", "city", "country", "owner")


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("title", "owner")


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):

    list_display = ("datetime_utc", "amount", "location", "payment", "owner")
    list_filter = ("datetime_utc", "amount", "location", "payment", "owner")

    fieldsets = (
        (None, {"fields": ("datetime_utc", "amount", "location", "payment", "owner")}),
        ("Media", {"fields": ("image", "document")}),
        ("Miscellaneous", {"fields": ("comment",)}),
    )


# admin.site.register(Document)
# admin.site.register(Picture)
