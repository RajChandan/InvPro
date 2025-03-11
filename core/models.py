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
