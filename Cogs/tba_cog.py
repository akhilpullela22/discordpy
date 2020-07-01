import requests

words = 30
paragraphs = 1
formats = 'text'
response = requests.get("https://www.thebluealliance.com/api/v3/status",
 headers={
   "X-TBA-Auth-Key": "wvbc47ZZiHo67u4tVA5oHDE7jeNzoWg8kiM3YP4R7PFuAl0M0GUfGoSfVVdjNb3g"
 }
)
print(response.text)