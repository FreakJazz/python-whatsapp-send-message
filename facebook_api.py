
# importing the requests library
import requests

# api-endpoint
URL = "https://graph.facebook.com/v15.0/107736935319648/v1/messages"
token = 'EAAFhebehDXcBALPhViRHeq7s7leFDpohnDUsGGpbUQwAkswN8wIKSEZAtJdzzfELjZCkWmQjuEXnJnAcfZAY9O3Aq58zzeeT0IB8V1wiZAPLteJaKhSSysvPc9ZCs3HBcM36zy6584mRBOLIGMUDe4DV4kt3Qq7JrEUIO22nigKnQInWp7ZBjtgYLEPEPVV04uDHaut6YRkUquThx2kgZCY'

headers =  { 'Authorization': 'Bearer ' + token, "Content-Type":"application/json"}

# data
data_template = {
    "messaging_product":"whatsapp",
"to": "593983551848",
"type": "template",
"template": { "name": "hello_world", "language": { "code": "en_US" } 
}}

data_custom = {
  "recipient_type": "individual",
  "to": "whatsapp-id",
  "type": "text",
  "text": {
      "body": "Hola, como estas es un gusto saludarte"
  }
}
  
# sending get request and saving the response as response object
r = requests.post(url = URL, json = data_template, headers=headers )
  
# extracting data in json format
data = r.json()
  
# extracting response text 
pastebin_url = r.text
print("The pastebin URL is:%s"%pastebin_url)