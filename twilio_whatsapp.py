import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
print(os.getenv('TWILIO_ACCOUNT_SID'))
# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
client = Client(os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN'))

# this is the Twilio sandbox testing number
from_whatsapp_number = os.getenv('TWILIO_NUMBER')
# NUMBER PERSONAL 
to_whatsapp_number = os.getenv('PERSONAL_NUMBER')

message = client.messages.create(
                            body='Hola como estas',      
                            from_='+14155238886',  
                            to='+593983551848') 

print(message.sid)



