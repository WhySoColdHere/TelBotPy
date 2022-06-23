import requests
from bs4 import BeautifulSoup

list_of_signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
                 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
list_of_signs = [i.lower() for i in list_of_signs]
i = 0

list_with_horoscope = []

while i <= 11:
    url = "https://horo.mail.ru/prediction/" + list_of_signs[i] + "/today/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    div_class_signs = 'article__item article__item_alignment_left article__item_html'
    a = soup.find('div', class_=div_class_signs)
    i += 1
    list_with_horoscope.append(a.text)

