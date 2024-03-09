from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

import requests

from .serializers import IPSerializer
from ..models import acharIP

class IPViewset(ModelViewSet):

    serializer_class = IPSerializer
    queryset = acharIP.objects.all()

    from rest_framework.routers import DefaultRouter