import requests,mmh3,base64
response = requests.get('https://app.ardoq.com/favicon.ico')
favicon = base64.encodebytes(response.content)
hash = mmh3.hash(favicon)
print(hash)