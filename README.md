# Connection Tester
> Um testador de conexão simples para te avisar quando sua conexão está ativa ou inativa onde quer que você esteja.

![](header.png)

## Getting Started

Esse projeto utiliza Python 3, então você precisará ter esta versão instalada no seu ambiente. Para instalar, acesse o site do [Python](https://www.python.org/downloads/) e baixe a versão 3.

### Prerequisites

Você precisará instalar algumas bibliotecas do Python para que tudo funcione corretamente. Para isso, abra o CMD na pasta do seu projeto e digite o seguinte comando:

```
pip install -r requirements.txt
```

### Installing

Precisamos configurar o TeleSign para o envio de mensagens e o ambiente para que o programa inicie com o Sistema Operacional.

#### Telesign

Utilizaremos o TeleSign para envio de SMS. Caso você não queira que o envio de SMS ocorra, apague as seguintes linhas de código:

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

Message Types:

| message_type | description
|-----|:------------------------------------:|
| OTP | One time passwords 						|
| ARN | Alerts, reminders, and notifications |
| MKT | Marketing traffic						   |

#### Enviroment

Para fazer com que o programa inicie com o Windows, precisaremos fazer alguns procedimentos.

1. Aperte a tecla ```Windows``` + ```R``` e digite ```shell:startup```.
2. Copie e cole o arquivo __connection_tester.pyw__ na pasta que abrirá.
3. Move a pasta __files__ para o local desejado.
4. Altere a seguinte linha de código para o local onde está o arquivo (por padrão é C:/files): ```playsound('C:/files/reconnected.wav', block=False)```
- Você também pode alterar o site em que você fará os testes de conexão mudando as seguintes linhas de código: ```get('http://www.google.com')```.

**It's done :)**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contributing

1. Fork it (https://github.com/doougui/connection-tester/fork)
2. Clone repository (```git clone https://github.com/yourname/connection-tester```)
3. Create your feature branch (```git checkout -b your_feature_name```)
4. Commit your changes (```git commit -am 'Add some changes'```)
5. Push to the branch (```git push origin your_feature_name```)
5. Create a new Pull Request
