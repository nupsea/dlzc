import requests
url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

data = {
    'url': 'https://habrastorage.org/webt/yf/_d/ok/yf_dokzqy3vcritme8ggnzqlvwa.jpeg'
}

response = requests.post(
    url,
    json=data
)

if response.headers.get('Content-Type') == 'application/json':
    result = response.json()
    print(result)
else:
    print("Non-JSON response:", response.text)

