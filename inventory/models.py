from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    asset_id = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

