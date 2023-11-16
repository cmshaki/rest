from rest_framework.routers import DefaultRouter

from products.viewsets import ProductGenericViewSet

router = DefaultRouter()
router.register("products-abc", ProductGenericViewSet, basename="product")

urlpatterns = router.urls
