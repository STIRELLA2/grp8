import requests
url = "http://52.15.224.240:8080/grp8"
data = 'My String Test'
response=requests.post(url, json=data)
print (response.status_code)
print (response)
