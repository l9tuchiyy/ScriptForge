import requests
from apiget import API_KEY

get = input('Введите города через запятую: ')
result = [word.strip() for word in get.split(",")]
info = []
try:
    for word in result:
        params = {
            'appid': API_KEY,
            'q': word,
            'lang': 'ru',
            'units': 'metric',}
        response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
        data = response.json()
        info.append({'name': data['name'],
                     'temp': data['main']['temp']})
except KeyError:
    print('Город не найден')

info.sort(key=lambda x: x["temp"], reverse=True)

for el,item in enumerate(info, start=1):
    print(f'{el}. {item['name']} - {round(item['temp'])}°C')
