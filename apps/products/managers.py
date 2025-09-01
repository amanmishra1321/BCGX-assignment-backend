from django.db import models

class ProductManager(models.Manager):
    def top_selling(self, limit=10):
        """Return top-selling products"""
        return self.order_by("-units_sold")[:limit]

    def low_stock(self, threshold=10):
        """Return products with low stock"""
        return self.filter(stock_available__lt=threshold)

    def highly_rated(self, min_rating=4.0):
        """Return products above a certain rating"""
        return self.filter(customer_rating__gte=min_rating)
