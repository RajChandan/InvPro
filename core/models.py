from django.db import models


# Create your models here.
class ContactMessage(models.Model):
    ORGANIZATION_CHOICES = [
        ("Investment_firm", "Investment Firm"),
        ("investor", "Investor"),
        ("startup", "StartUp"),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    company = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    organization_type = models.CharField(
        max_length=50, choices=ORGANIZATION_CHOICES, blank=True
    )
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} --- {self.email} --- {self.message}"


class InvestmentInquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True, null=True)
    investment_amount = models.DecimalField(max_digits=12, decimal_places=2)
    investment_goal = models.CharField(max_length=255)
    risk_tolerance = models.CharField(max_length=50, blank=True, null=True)
    sectors = models.CharField(max_length=255, blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.investment_goal}"
