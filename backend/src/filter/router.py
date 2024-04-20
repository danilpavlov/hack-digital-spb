import os
from parser import parse_etu
from filter_wrapper import FilterWrapper

data_url = 'backend/src/filter/data/Данные приёмной кампании.csv'
profs_url = 'backend/src/filter/data/prof.csv'


if not os.path.exists(profs_url):
    parse_etu()

filter_wrap = FilterWrapper(data_url, profs_url)

test_atr = {
    'subjects': ['Математика', 'Информатика', 'Русский язык'],
    'scores': [100, 100, 100],

    'profession': ['Разработчик компьютерных программ (программист)', 'Тимлид']  # Желаемая профессия'
}

print(filter_wrap.get_documents(test_atr))