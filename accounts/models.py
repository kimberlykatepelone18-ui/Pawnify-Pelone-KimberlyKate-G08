from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        APPRAISER = 'appraiser', 'Appraiser'
        CASHIER = 'cashier', 'Cashier'
        CUSTOMER = 'customer', 'Customer'

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.CUSTOMER)
    contact_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    profile_photo = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.is_superuser:          # createsuperuser -> Admin role
            self.role = self.Role.ADMIN
        super().save(*args, **kwargs)

    def get_dashboard_url(self):
        return f'{self.role}_dashboard'   # url names: admin_dashboard, etc.

    def __str__(self):
        return f'{self.username} ({self.get_role_display()})'