import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import django
import csv

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'price_optimization_backend.settings')
django.setup()

from apps.products.models import Product

CSV_FILE = "product_data.csv"  # path to your CSV file

def import_products():
    with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            product, created = Product.objects.get_or_create(
                product_id=row["product_id"],
                defaults={
                    "name": row["name"],
                    "description": row.get("description", ""),
                    "cost_price": row["cost_price"],
                    "selling_price": row["selling_price"],
                    "category": row["category"],
                    "stock_available": row["stock_available"],
                    "units_sold": row.get("units_sold", 0),
                    "customer_rating": row.get("customer_rating") or None,
                    "demand_forecast": row.get("demand_forecast") or None,
                    "optimized_price": row.get("optimized_price") or None,
                },
            )
            if created:
                print(f"Inserted: {product.name}")
            else:
                print(f"Skipped (already exists): {product.name}")

if __name__ == "__main__":
    import_products()
