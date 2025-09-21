from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    """Extended user model for StrataAI with role-based access"""
    
    class Role(models.TextChoices):
        RESIDENT = 'resident', 'Resident'
        GUARD = 'guard', 'Security Guard'
        ADMIN = 'admin', 'Admin'
        HOA_OFFICER = 'hoa_officer', 'HOA Officer'
        MAINTENANCE_STAFF = 'maintenance_staff', 'Maintenance Staff'
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.CharField(max_length=20, blank=True)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.RESIDENT)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    fcm_token = models.TextField(blank=True, null=True)  # For push notifications
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.get_full_name()} ({self.username}) - {self.role}"
