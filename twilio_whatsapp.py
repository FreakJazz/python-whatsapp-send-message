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
                            media_url=['/static/Loading-Resultados-02.gif']
                            body='Hola te invito a ver este video',      
                            from_='whatsapp:+14155238886',  
                            to='whatsapp:+593987016344') 

print(message.sid)



