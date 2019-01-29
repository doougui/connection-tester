from __future__ import print_function
from time import sleep
from datetime import datetime
from playsound import playsound
from requests import get
from requests import exceptions
from telesign.messaging import MessagingClient

customer_id = "C765DCA3-324C-4812-87F8-7D13ECE90BE2"
api_key = "+sDtoZC6HVB6esmkapaRjdxxtnZG9XHWFK/pH1YljzpusZPDrxzykS2CnZrbSbdFLAzLXUU7eJhL2ZwsADZLxg=="

phone_number = "+5548999751669"
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

    playsound('files/disconnected.wav', block=False)

    now = datetime.now()
    while True:
        sleep(5)
        try:
            get('http://www.google.com')
            message = "Reconnected. The connection was lost on: {}.".format(now.strftime("%Y-%m-%d %H:%M"))
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
