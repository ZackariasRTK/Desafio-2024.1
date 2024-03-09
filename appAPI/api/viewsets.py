from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

import requests

from .serializers import IPSerializer
from ..models import acharIP

class IPViewset(ModelViewSet):

    serializer_class = IPSerializer
    queryset = acharIP.objects.all()

    def pegarIP(self, request):
        ip = request.data.get('ip','')

        linkIP = (f'https://ipapi.co/{ip}/json/') # Cria uma url da API externa usando o ip fornecido

        requisicao = requests.get(linkIP)  # Requisição à API através do link 

        json = requisicao.json() 

        ip = json.get('ip','')  # Procura os dados através do método GET
        cidade = json.get('city', '')
        regiao = json.get('region','')
        paisC = json.get('country_code', '')
        paisN = json.get('country_name', '')
        capital = json.get('country_capital','')

        dadosreceb = {     # Guarda os dados extraídos
            "ip": f'{ip}',
            "city": f'{cidade}',
            "region": f'{regiao}',
            "country_code": f'{paisC}',
            "country_name": f'{paisN}',
            "country_capital": f'{capital}'
        }

    
        meuSerializer = IPSerializer(data=dadosreceb)

        if meuSerializer.is_valid():

            # Lê o IP inserido para buscar se o IP já existe no banco de dados
            ipPesquisado = acharIP.objects.filter(ip=ip) 
            ipPesquisadoExiste = ipPesquisado.exists()     

            if ipPesquisadoExiste:
                return Response({"Aviso!":"Este IP já consta no banco de dados!"}) 
            
            # Caso um mesmo IP tente ser inserido, retornará a resposta acima, senão, adicionará o IP no banco.
            

            meuSerializer.save()
            return Response(meuSerializer.data)
        
        else:
            return Response({"Oops..: Algo deu errado!"}) # Em caso de erro, esta mensagem será enviada
