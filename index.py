import os
from twilio.rest import Client
from dotenv import load_dotenv
import pandas as pd
from airtable import airtable


load_dotenv()  # take environment variables from .env.

def main ():
    client = Client(os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN'))
    database = airtable.Airtable(os.getenv('AIRTABLE_DATABASE'), os.getenv('AIRTABLE_APIKEY'))
    database.get(os.getenv('AITABLE_TABLE'))

    data = pd.read_excel('data.xlsx')
    print(data)
    names = data['nombres']
    phones = data['telefono1']
    phones2 = data['telefono2']
    print(names, phones, phones2)

    # for i in range (0, len(names)):
    #     phone = 'whatsapp:+593'+str(phones[i])
    #     name = str(names[i])

    #     message = client.messages.create(
    #                             body='Hola '+ name +', te invito a ver este video  ',      
    #                             from_='whatsapp:+14155238886', 
    #                             media_url='https://firebasestorage.googleapis.com/v0/b/cne2023-772c8.appspot.com/o/agendas%2Fobserver_international%2F21e1b90a-859c-42cc-b9cf-480242f40d4b?alt=media&token=eda3d9c6-89b2-412e-a423-3b8a4a642843',
                                
    #                             media_url='https://firebasestorage.googleapis.com/v0/b/cne2023-772c8.appspot.com/o/agendas%2FVID-20230124-WA0079.mp4?alt=media&token=4ba36325-c9a8-4d3f-a343-5ae8af34d6c2',
    #                             to= phone
    #                             ) 
    #     print(message.sid)

if __name__ == "__main__": 

    main()