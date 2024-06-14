from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'purchase_orders', PurchaseOrderViewSet)
router.register(r'purchase_order_items', PurchaseOrderItemViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
