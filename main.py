# import requests
# url = "https://rickandmortyapi.com/api/character/"
# r = requests.get(url)
# data = r.json()
# data = data['results']
# for i in data:
#     name = i['name']
#     status = i['status']
#     origin = i['location']
#     print(name,status, origin)
#     with open('info.txt', 'a') as file:
#         file.write(f'Имемя: {name}\n')
#         file.write(f'Статус: {status}\n')
#         file.write(f'Оригинал: {origin}')
# print(name)
# print(status)
# print(origin)

from curses import halfdelay
import requests
import json
from config import API
from pprint import pprint
from datetime import datetime


def furunkl(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric"
    r = requests.get(url)
    data = r.json()
    city = data['name']
    cur_weather = data['main']['temp']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    sunrise_timepesmp = datetime.fromtimestamp(data['sys']['sunrise'])
    sunset_timepesmp = datetime.fromtimestamp(data['sys']['sunset'])
    length_of_the_day = sunset_timepesmp - sunset_timepesmp
    weather_description = data['weather'][0]['main']

    text = f"""
    Дата: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    Погода в городе: {city}
    Температура: {cur_weather}
    Влажность: {humidity}
    Давление: {pressure} мм.рт.ст
    Скорость ветра: {wind}
    Восход: {sunrise_timepesmp}
    Продолжительность дня: {length_of_the_day}
    Закат: {sunset_timepesmp}
    """
    return text




