# apps/products/permissions.py
from rest_framework.permissions import BasePermission, SAFE_METHODS

class ProductPermission(BasePermission):
    """
    Custom role-based access control:
    - Admin: Full access
    - Buyer: Read-only
    - Supplier: Can view + add, but not update/delete
    """

    def has_permission(self, request, view):
        user = request.user
        print("user",user)

        if not user.is_authenticated:
            return False  # must be logged in

        # Admin => full access
        if user.role == "admin":
            return True  

        # Buyer => Read-only (GET, HEAD, OPTIONS)
        if user.role == "buyer":
            return request.method in SAFE_METHODS

        # Supplier => Read + Create
        if user.role == "supplier":
            return request.method in SAFE_METHODS or request.method == "POST"

        return False  # default deny
