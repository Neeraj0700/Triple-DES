import os
from twilio.rest import Client

account_sid = 'ACd138af6647dbc2811972df9bae2815fe'
auth_token = 'fd5b366509aa4af1c5384718dae52e07'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='Hii Babu!',
         from_='+18645138747',
         to='+919354433899'
     )

print(message.sid)
