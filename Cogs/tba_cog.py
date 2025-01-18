import requests

words = 30
paragraphs = 1
formats = 'text'
response = requests.get("https://www.thebluealliance.com/api/v3/status",
 headers={
   "X-TBA-Auth-Key": "auth-key"
 }
)
print(response.text)
