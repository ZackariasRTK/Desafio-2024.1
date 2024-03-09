from rest_framework.routers import DefaultRouter
from .viewsets import IPViewset

from django.urls import path, include

router = DefaultRouter()
router.register(prefix="ip",viewset=IPViewset)

urlpatterns = [

    # Inclua os caminhos aqui

    path("api/",include(router.urls))

    #htts://../api/ip/

]