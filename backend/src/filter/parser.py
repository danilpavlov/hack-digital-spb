import requests
from bs4 import BeautifulSoup
import time
import pandas as pd


def parse_etu():
    url = 'https://abit.etu.ru/ru/postupayushhim/bakalavriat-i-specialitet/napravleniya-podgotovki/'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser', )

    links = soup.find_all('a',
                          class_='btn btn-primary direction-content__more d-flex justify-content-center align-items-center'
                          )
    profs = []

    for link in links:
        direction_url = 'https://abit.etu.ru/' + link['href']

        response = requests.get(direction_url)

        soup = BeautifulSoup(response.text, 'html.parser')
        time.sleep(2)

        try:
            profession_names = soup.find_all('div',
                                             class_='who-work__profession-name')  # Находим все элементы с классом
            for profession_name in profession_names:
                profession_name_text = profession_name.text.strip()
                program_name = soup.find('div', class_='direction-title').text.strip()
                program_name = ' '.join(program_name.split(' ')[1:])  # Убираем дату в названии
                profs.append((profession_name_text, program_name))

        except:
            print('Failed parsing...')

    profs_df = pd.DataFrame(data={
        'Конкурсн. группа': [prof[1] for prof in profs],
        'Профессия':  [prof[0] for prof in profs],
        }
    )
    profs_df.to_csv('./backend/src/filter/data/prof.csv')
