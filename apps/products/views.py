from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer
from .permissions import ProductPermission

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing products.
    """
    queryset = Product.objects.all().order_by('-product_id')
    serializer_class = ProductSerializer
    permission_classes = [ProductPermission]
