from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# Register viewsets here:
# router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
