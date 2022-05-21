from twilio.rest import Client
TWILIO_ACCOUNT_SID='AC0ccf3b91bd30a8276d87212348ae6a56'
TWILIO_AUTH_TOKEN='9a08e831ec537e4d0b73767b3f296d35'
# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# this is the Twilio sandbox testing number
from_whatsapp_number='+14155238886'
# replace this number with your own WhatsApp Messaging number
to_whatsapp_number='+593983551848'

message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Hola como estas',      
                              to='whatsapp:+593983551848' 
                          ) 

print(message.sid)



