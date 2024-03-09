from rest_framework.serializers import ModelSerializer
from ..models import acharIP

class IPSerializer(ModelSerializer):
    class Meta: 
        model = acharIP
        fields = ['id','ip','','cidade','regiao','paisC','paisN', 'capital']