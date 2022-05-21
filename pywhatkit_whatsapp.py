import pywhatkit as pwk
from flask import Flask
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
# using Exception Handling to avoid unexpected errors
try:
     # sending message in Whatsapp in India so using Indian dial code (+91)
     pwk.sendwhatmsg("+593964091474", "Test send message automatic?", 14,41, False)
 
     print("Message Sent!") #Prints success message in console
 
     # error message
except: 
     print("Error in sending the message")




