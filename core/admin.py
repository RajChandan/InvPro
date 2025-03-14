from django.contrib import admin
from .models import ContactMessage, InvestmentInquiry

# Register your models here.


@admin.register(ContactMessage)
# @admin.register(InvestmentInquiry)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "company",
        "phone",
        "organization_type",
        "submitted_at",
    )
    search_fields = ("name", "email", "company", "message")
    list_filter = ("organization_type", "submitted_at")
