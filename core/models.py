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


class Startup(models.Model):
    INDUSTRY_CHOICES = [
        ("technology", "Technology"),
        ("healthcare", "Healthcare"),
        ("fintech", "Fintech"),
        ("education", "Education"),
        ("ecommerce", "E-commerce"),
        ("other", "Other"),
    ]
    STAGE_CHOICES = [
        ("idea", "Idea Stage"),
        ("mvp", "MVP"),
        ("early", "Early Traction"),
        ("growth", "Growth Stage"),
        ("scaling", "Scaling"),
    ]

    startup_name = models.CharField(max_length=200)
    company_url = models.URLField(blank=True)
    email = models.EmailField()
    description = models.TextField(blank=True)
    founder_name = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    industry = models.CharField(
        max_length=50, choices=INDUSTRY_CHOICES, default="other"
    )
    startup_stage = models.CharField(
        max_length=50, choices=STAGE_CHOICES, default="idea"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.startup_name
