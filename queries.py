import requests
from time import sleep


def request_local_server(login, password):
    data = {'login': login, 'password': password}
    response = requests.post('http://127.0.0.1:5000/auth', json=data)
    return response.status_code == 200


def request_local_server_protected(login, password):
    data = {'login': login, 'password': password}
    attempts = 3

    for i in range(attempts):
        try:
            response = requests.post('http://127.0.0.1:4000/auth', json=data)
            if response.status_code == 200:
                return True
            elif response.status_code == 401:
                return False
        except:
            pass

        if i != attempts - 1:
            sleep(1)

    return False
