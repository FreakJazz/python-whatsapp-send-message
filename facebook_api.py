
# importing the requests library
import requests

# api-endpoint
URL = "https://graph.facebook.com/v15.0/107736935319648/v1/messages"
token = 'EAAFhebehDXcBANrZCn4cFHJ7l3p21zdIfgPIlhIi887Mt2L4UbZC7hyZCTrvNALOQLrVTBIYwRcrl6iqSiXbfpewVmvoFrZAOY21GyK7VqVqw84hqxR3EuzSfBAPamrmAqqlSgrIXJg6oBvOCPhTs0mIGZBlZB2V3xrKTl3NrsNW8x97ZBpxCp1IbkG79cvgQtxFNGWvZBK8sPQ3lZCRjHrxZC'

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
r = requests.post(url = URL, json = data_custom, headers=headers )
  
# extracting data in json format
data = r.json()
  
# extracting response text 
pastebin_url = r.text
print("The pastebin URL is:%s"%pastebin_url)