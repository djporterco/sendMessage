
# coding: utf-8

# https://www.twilio.com/docs/notify/quickstart/sms

from twilio.rest import Client

def sendmessage(body):
        sid = '[YOUR_SID_CODE_HERE]'
    auth_token ='[YOUR_AUTH_CODE_HERE]'
    client = Client(sid, auth_token)
    message = client.messages.create(to="[YOUR_NUMBER]",from_="[YOUR_TWILIO_NUMBER]  ",body=body)

sendmessage('test')
