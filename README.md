# Connection Tester
> A simple connection tester to let you know when your connection is online or offline wherever you are.

![](header.png)

## Getting Started

This project uses Python 3, so you will need to have this version installed in your device. To install, go to the [Python](https://www.python.org/downloads/) website and download version 3.

### Prerequisites

You will need to install some Python libraries so that everything works correctly. To do this, open the CMD in the folder of your project and enter the following command:

```
pip install -r requirements.txt
```

### Installing

It is necessary to configure TeleSign to send messages and it is also necessary to configure the environment for the program to start with the OS.

#### TeleSign

TeleSign is required for sending messages. If you don't want to send SMS, delete the following lines of code:

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

If you want the SMS service, follow these steps:

1. Sign up to [TeleSign](https://portal.telesign.com).
2. Verify your account with your phone number.
3. Copy your __Customer ID__ and paste in ```customer_id``` variable.
4. Copy your __API Key__ and paste in ```api_key``` variable.
5. Inside the [TeleSign Dashboard](https://portal.telesign.com/portal/dashboard), go to *Settings -> Test Numbers*.
6. Add your number by clicking the __Add a Number__ button.
7. Add your phone number to the ```phone_number``` variable.
8. If you want, you can change the message and the type of the message you will receive.

Message Types:

| message_type | description
|-----|:------------------------------------:|
| OTP | One time passwords 						|
| ARN | Alerts, reminders, and notifications |
| MKT | Marketing traffic						   |

#### Enviroment

To make the program start with Windows, some procedures need to be done.

1. Press the ```Windows``` + ```R``` key and type ```shell:startup```.
2. Copy and paste the __connection_tester.pyw__ file on the folder that will open.
3. Move the __files__ folder to your desired location.
4. Change the following line of code to the location where the file is located: ```playsound('files/reconnected.wav', block=False)```
- You can also change the website where you will do the connection tests by changing the following lines of code: ```get('http://www.google.com')```.

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

The more you help, the better. So feel free to help as much as you want (Mainly with translations).