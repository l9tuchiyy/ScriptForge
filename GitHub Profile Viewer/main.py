import requests

username = input("Введите GitHub юзернейм: ")
response = requests.get(f'https://api.github.com/users/{username}')
data = response.json()

if response.status_code == 200:
    print(f'👤{data['name']}\n\n'
          f'Логин: {data['login']}\n'
          f'Репозиториев: {data['public_repos']}\n'
          f'Подписчиков: {data['followers']}\n'
          f'Подписок: {data['following']}\n'
          f'Создан аккаунт: {data['created_at']}')
else:
    print(f'Ошибка! [{response.status_code}]')