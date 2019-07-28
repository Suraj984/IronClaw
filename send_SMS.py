import os
from twilio.rest import Client

account_sid = "AC9e44bcb5e78a0485f937aa6385b2963b"
auth_token = "de12467dfb148c7e95481fce59be8d36"

client = Client(account_sid, auth_token)

message = client.messages.create(body="Warning!!!, Natural Calamity bound to happen!!",
									to='+91-9613342897',
									from_='+14158141829')
print(message.sid)
