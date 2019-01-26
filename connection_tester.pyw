from __future__ import print_function
from time import sleep
from playsound import playsound
from requests import get
from requests import exceptions
from telesign.messaging import MessagingClient

customer_id = "Your customer key"
api_key = "Your API Key"

phone_number = "Your phone number"
message = "Reconnected"
message_type = "ARN"

messaging = MessagingClient(customer_id, api_key)

def checkInternetConnection(errCount = [0]):
    try:
        get('http://www.google.com')
        errCount[0] = 0
        print('Connected.')
    except exceptions.ConnectionError as err:
        errCount[0] += 1
        print('Connection error{}: {}'.format(errCount, err))
        if errCount[0] == 3:
            errCount[0] = 0
            checkReconnection()

def checkReconnection():
    print('Starting the connection detection mode.')
    while True:
        sleep(5)
        try:
            get('http://www.google.com')
            response = messaging.message(phone_number, message, message_type)
            playsound('files/reconnected.wav', block=False)
            print('Reconnected. Returning to the connection checker.')
            break
        except exceptions.ConnectionError:
            print('Disconnected.')
            continue

while True:
    sleep(5)
    checkInternetConnection()
