from django.db import models
from django.contrib.auth.models import User  # Import the User model
# Create your models here.
import uuid

# views.py
    
class Customer(models.Model):
    id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4,
        editable = False, 
        unique=True
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # name= models.CharField(max_length=200)
    # email= models.CharField(max_length=100)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.id