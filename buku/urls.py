from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BukuViewSet

router = DefaultRouter()
router.register(r'buku', BukuViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
