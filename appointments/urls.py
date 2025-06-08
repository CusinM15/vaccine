from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VaccineViewSet

router = DefaultRouter()
router.register(r'vaccines', VaccineViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
