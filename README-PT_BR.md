# Connection Tester
> Um testador de conexão simples para te avisar quando sua conexão está ativa ou inativa onde quer que você esteja.

![](header.png)

## Começando

Esse projeto utiliza Python 3, então você precisará ter esta versão instalada no seu dispositivo. Para instalar, acesse o site do [Python](https://www.python.org/downloads/) e baixe a versão 3.

### Pré-requisitos

Você precisará instalar algumas bibliotecas do Python para que tudo funcione corretamente. Para isso, abra o CMD na pasta do seu projeto e digite o seguinte comando:

```
pip install -r requirements.txt
```

### Instalando

É necessário configurar o TeleSign para o envio de mensagens e também é necessário configurar o ambiente para que o programa inicie com o Sistema Operacional.

#### TeleSign

O TeleSign é necessário para o envio de menssagens. Caso você não queira que o envio de SMS ocorra, apague as seguintes linhas de código:

```
from telesign.messaging import MessagingClient

customer_id = "Your customer key"
api_key = "Your API Key"

phone_number = "Your phone number"
message = "Reconnected"
message_type = "ARN"

messaging = MessagingClient(customer_id, api_key)
```
```
response = messaging.message(phone_number, message, message_type)
```

Caso você queira o serviço de SMS, siga os seguintes passos:

1. Registre-se no [TeleSign](https://portal.telesign.com).
2. Verifique sua conta com seu número de telefone.
3. Copie o seu __Customer ID__ e cole na variável ```customer_id```.
4. Copie sua __API Key__ e cole na variável ```api_key```.
5. Dentro do [TeleSign Dashboard](https://portal.telesign.com/portal/dashboard), acesse *Settings -> Test Numbers*.
6. Adicione o seu número clicando no botão __Add a Number__.
7. Adicione o seu número de telefone na variável ```phone_number```.
8. Se quiser, você pode mudar a mensagem e o tipo da mensagem que você irá receber. 

Tipos de mensagens:

| tipo_de_mensagem | descrição
|-----|:------------------------------------:|
| OTP | Senhas						               |
| ARN | Alertas, lembretes, e notificações   |
| MKT | Marketing						            |

#### Ambiente

Para fazer com que o programa inicie com o Windows, precisaremos fazer alguns procedimentos.

1. Aperte a tecla ```Windows``` + ```R``` e digite ```shell:startup```.
2. Copie e cole o arquivo __connection_tester.pyw__ na pasta que abrirá.
3. Mova a pasta __files__ para o local desejado.
4. Altere a seguinte linha de código para o local onde está o arquivo: ```playsound('files/reconnected.wav', block=False)```
- Você também pode alterar o site em que você fará os testes de conexão mudando as seguintes linhas de código: ```get('http://www.google.com')```.

**Está feito :)**

## Licença

Este projeto é linceciado na licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para detalhes.

## Contribuindo

1. Faça um Fork (https://github.com/doougui/connection-tester/fork)
2. Clone o repositório (```git clone https://github.com/yourname/connection-tester```)
3. Crie o branch da sua alteração (```git checkout -b your_feature_name```)
4. Commite as suas mudanças (```git commit -am 'Add some changes'```)
5. Faça um push no branch (```git push origin your_feature_name```)
5. Crie uma nova PR. 

Quanto mais ajuda, melhor, então sinta-se a vontade para contribuir o quanto quiser.
