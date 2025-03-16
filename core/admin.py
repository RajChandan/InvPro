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


@admin.register(InvestmentInquiry)
class InvestInquiryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "phone",
        "investment_amount",
        "investment_goal",
        "risk_tolerance",
        "sectors",
        "submitted_at",
    )
    search_fields = ("name", "email", "sectors")
