# Desafio referente ao Back-End da Fábrica de Software - 2024.1

### Resumo breve do que irá ser abordado 📌
 Consiste em ler os dados de uma api externa (https://ipapi.co/185.124.201.182/json/) e retornar o IP e os respectivos dados automaticamente.
## Requerimentos 📋
Antes de tudo, é de suma importância ter o Python instalado, além de ser indispensável a criação de um ambiente virtual e a instalação de dependências essenciais.
```
py -m venv (nome da venv) - # Criação da venv com o nome desejado
.\(nome da venv)\Scripts\activate - # Comando para entrar na venv; Caso ocorra bloqueio ⛔, utlize 'Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass'
```
Ademais, instale as seguintes dependências:
```
pip install django djangorestframework
pip install requests
```
## Como acessar a API 🖥️
Em seu terminal, certifique-se de realizar, dentro da venv, os seguintes comandos:
```
py manage.py makemigrations
py manage.py migrate
```
Em seguida, para abrir o servidor local, use:
```
py manage.py runserver
```
Ao realizar o ```runserver```, um IP local será definido (http://127.0.0.1:8000/), com isso, deve-se adicionar o encaminhamento correto ```http://127.0.0.1:8000/api/ip/```

## Insomnia - GET, POST, DELETE 🌐
**AVISO:** ```import requests``` é vital neste momento!

Configurando a função 'create' no viewsets.py da pasta 'api', a função recebe o atributo sob a API em si.

Eu resolvo definir um valor padrão para 'ip', em conformidade com o input, em método POST.
```
ip = request.data.get('ip','')
```
Defino uma outra variável, 'linkIP', que usa {ip} (ip fornecido), fornecendo as informações do ip desejável e então crio 'requisicao' para utilizar o método GET com base em 'linkIP'.

A variável 'json' serve apenas para certificar de que a resposta esteja em formato JSON.
```
linkIP = (f'https://ipapi.co/{ip}/json/') 
requisicao = requests.get(linkIP) 
json = requisicao.json()
```
Por conseguinte, defino quais informações devem ser requeridas e inicio um dicionário para armazená-las.

```
ip = json.get('ip','') 
cidade = json.get('city', '')
regiao = json.get('region','')
paisC = json.get('country_code', '')
paisN = json.get('country_name', '')
capital = json.get('country_capital','')

 dadosreceb = {     
            "ip": f'{ip}',
            "city": f'{cidade}',
            "region": f'{regiao}',
            "country_code": f'{paisC}',
            "country_name": f'{paisN}',
            "country_capital": f'{capital}'
        }
```
❗**AVISO:** Em teoria, seria possível o retorno das demais informações de forma automática e a confirmação ou não de que há dados repetidos no banco de dados, no entanto, por causa de algum erro de minha parte, os campos não recebem os devidos valores e é possível repetir o mesmo IP diversas vezes.

E então, um algoritmo para controlar os requests, tendo em consideração se há ou não uma repetição de valores.
```
meuSerializer = IPSerializer(data=dadosreceb)

        if meuSerializer.is_valid():

            ipPesquisado = acharIP.objects.filter(ip=ip) 
            ipPesquisadoExiste = ipPesquisado.exists()     

            if ipPesquisadoExiste:
                return Response({"Aviso!":"Este IP já consta no banco de dados!"}) 
            
        
            meuSerializer.save()
            return Response(meuSerializer.data)
        
        else:
            return Response({"Oops..: Algo deu errado!"}) # Em caso de erro, esta mensagem será enviada
```
