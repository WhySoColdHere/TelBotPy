import json
import requests

url = 'https://www.cbr-xml-daily.ru/daily_json.js'

response = requests.get(url).content

data = json.loads(response)

GBP = [data['Valute']['GBP']['CharCode'],
       data['Valute']['GBP']['Nominal'],
       data['Valute']['GBP']['Value']]

USD = [data['Valute']['USD']['CharCode'],
       data['Valute']['USD']['Nominal'],
       data['Valute']['USD']['Value']]

EUR = [data['Valute']['EUR']['CharCode'],
       data['Valute']['EUR']['Nominal'],
       data['Valute']['EUR']['Value']]

JPY = [data['Valute']['JPY']['CharCode'],
       data['Valute']['JPY']['Nominal'],
       data['Valute']['JPY']['Value']]

list_of_money = [GBP, USD, EUR, JPY]


