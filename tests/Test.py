import requests
from datetime import datetime

site_list = ['https://novasport.md/', 'https://sportpitt.md/', 'https://proteinhouse.md/', 'https://www.suplimente.md/',
             'https://shop.bigsport.md/ru/supliments/']
site_list_1 = ['https://novasport.md/', 'https://novasport.md/', 'https://novasport.md/', 'https://novasport.md/',
               'https://novasport.md/']


# for r in range(10):
#     session = requests.Session()
#     adapter = requests.adapters.HTTPAdapter(
#         pool_connections=100,
#         pool_maxsize=100)
#     session.mount('http://', adapter)
#     response = session.get('https://novasport.md/')
#     print(response.raise_for_status())

def generate_requests():
    t_1 = datetime.now()
    for l in site_list_1:
        for i in range(10):
            t_2 = datetime.now()
            res = requests.get(l)
            print(l, res.status_code, i, t_2 - t_1)

generate_requests()
# for r in range(101):
#     generate_requests()
