from django.db import models
from .managers import ProductManager

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)  # Auto-incremented ID
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    stock_available = models.PositiveIntegerField()
    units_sold = models.PositiveIntegerField(default=0)
    customer_rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)  # e.g. 4.5
    demand_forecast = models.FloatField(blank=True, null=True)  # Predicted demand (can be updated later)
    optimized_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)  # When product was created
    updated_at = models.DateTimeField(auto_now=True)      # When product was last updated

    objects = ProductManager()  
    
    def __str__(self):
        return f"{self.name} ({self.category})"
