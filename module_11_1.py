import pprint
import pandas as pd
import requests

# pandas
df = pd.read_csv('titanic.csv') # чтение файла

print(df.info()) # вся информация
print(df.shape) # сколько строк и столлбцов
print(df.columns) # какие загаловки столбцов
print(df['Sex']) # вывод столбца "Sex"
print(df[(df['Sex'] == 'male')][['Age','Name']].head(10)) # Вывод всех мужчин с указанием их возрастаа и имени

# requests
response = requests.get(url='https://www.google.ru/')  # запрос на сайтт

print(response.status_code)  # статус кода
print(response.ok)  # смог ли подключится

response2 = requests.get('https://api.github.com/')  #
response2_json = response2.json()  # записать информацию с сайта в формате json
pprint.pprint(response2_json)  # удобный вывод

print(response2.headers)  # вывод заголовков
print(response2.request.headers)  # заголовки запросов

user_agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
response2 = requests.get('https://api.github.com/', headers=user_agent)  # оправка завроса с измененым  User-Agent
response2_json = response2.json()  #

print(response2.headers)  #
print(response2.request.headers)  #
