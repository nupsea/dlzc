import requests
# url = 'http://localhost:8080/2015-03-31/functions/function/invocations'
url = 'https://e6nrpdco19.execute-api.ap-southeast-2.amazonaws.com/cc-test-ws/predict'

data = {
    'url': 'http://bit.ly/mlbookcamp-pants'
}

result = requests.post(
    url,
    json=data
).json()

print(result)