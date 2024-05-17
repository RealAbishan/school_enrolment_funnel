from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FunnelStatusViewSet, StudentViewSet, StatusLogViewSet

router = DefaultRouter()
router.register(r'funnel-status', FunnelStatusViewSet)
router.register(r'students', StudentViewSet)
router.register(r'logs', StatusLogViewSet, basename='statuslog')

urlpatterns = [
    path('', include(router.urls)),
]
