import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
client = Client(os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN'))

# this is the Twilio sandbox testing number
from_whatsapp_number = os.getenv('TWILIO_NUMBER')
# NUMBER PERSONAL 
to_whatsapp_number = os.getenv('PERSONAL_NUMBER')

message = client.messages.create(
                            to='whatsapp:+593983551848',
                            from_='whatsapp:+14155238886',  

                            body='Hola te invito a ver este video', 
                            media_url={'https://firebasestorage.googleapis.com/v0/b/cne2023-772c8.appspot.com/o/agendas%2FVID-20230124-WA0079.mp4?alt=media&token=4ba36325-c9a8-4d3f-a343-5ae8af34d6c2'},

                            # media_url=['https://firebasestorage.googleapis.com/v0/b/cne2023-772c8.appspot.com/o/agendas%2Fobserver_international%2F21e1b90a-859c-42cc-b9cf-480242f40d4b?alt=media&token=eda3d9c6-89b2-412e-a423-3b8a4a642843'],

                            content_sid= 'Hola te invito a ver este video',)     

print(message.status)
