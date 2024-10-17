import requests


# URI for the API enpoint

url='http://api.github.com'

response = requests.get(url)

#check if it successful or not

if response.status_code==200:
    print('successful!!')
    print(response.json())

if response.status_code!=200:
    print(f'Failed with status code: {response.status_code}')

