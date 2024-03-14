from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors134400ViewSet

router = DefaultRouter()
router.register(
    "testconnectors134400", Testconnectors134400ViewSet, basename="testconnectors134400"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
