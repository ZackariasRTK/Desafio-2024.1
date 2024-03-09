from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

import requests

from .serializers import IPSerializer
from ..models import acharIP

class IPViewset(ModelViewSet):

    serializer_class = IPSerializer
    queryset = acharIP.objects.all()

    def pegarIP(self, request):
        ip = request.data.get('ip','000000000000')

        linkIP = (f'https://ipapi.co/{ip}/json/') # link com o ip desejável

        requisicao = requests.get(linkIP)  # meio para acessar o link

        json = requisicao.json()

        ip = json.get('ip','')  # Procura os dados através do método GET
        cidade = json.get('logradouro', '')
        regiao = json.get('complemento','')
        cidade = json.get('city', '')
        regiao = json.get('region','')
        paisC = json.get('country_code', '')
        paisN = json.get('country_name', '')
        capital = json.get('country_capital','')

        dadosreceb = {     # Guarda os dados
            "ip": f'{ip}',
            "city": f'{cidade}',
            "region": f'{regiao}',
            "country_code": f'{paisC}',
            "country_name": f'{paisN}',
            "country_capital": f'{capital}'
        }

    
        meuSerializer = IPSerializer(data=dadosreceb)

        if meuSerializer.is_valid():

            ipPesquisado = acharIP.objects.filter(ip=ip) 

            # Lê o IP inserido para buscar no banco de dados

            ipPesquisadoExiste = ipPesquisado.exists()        

            if ipPesquisadoExiste:
                return Response({"Aviso!":"Este IP já consta no banco de dados!"}) 
            
            # Caso um mesmo IP tente ser inserido, retornará a resposta acima, senão, adicionará o IP no banco.
            

            meuSerializer.save()
            return Response(meuSerializer.data)
        
        else:
            return Response({"Oops..: Algo deu errado!"}) # Em caso de erro, esta mensagem será enviada
