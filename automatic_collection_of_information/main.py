import requests
headers = {
    'Host': 'hh.ru',
    'User-agent': 'Chrome',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}
hh_request = requests.get('https://hh.ru/search/vacancy?items_on_page=100&text=qa+engineer', headers=headers)
print(hh_request.text)