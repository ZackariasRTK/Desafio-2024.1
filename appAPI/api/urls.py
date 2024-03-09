from rest_framework.routers import DefaultRouter
from .viewsets import IPViewset
from django.urls import path, include

router = DefaultRouter()
router.register(prefix="ip",viewset=IPViewset)

urlpatterns = [
    path("api/",include(router.urls))
]