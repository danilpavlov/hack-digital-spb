import os
from parser import parse_etu
from filter_wrapper import FilterWrapper

data_url = 'backend/src/filter/data/Данные приёмной кампании.csv'
profs_url = 'backend/src/filter/data/prof.csv'


if not os.path.exists(profs_url):
    parse_etu()

filter_wrap = FilterWrapper(data_url, profs_url)

test_atr = {
    'exam_1_name': 'Математика',  # Название первого экзамен
    'exam_1_score': 100,  # Баллы за 1 экзамен

    'exam_2_name': 'Информатика',  # Название второго экзамен
    'exam_2_score': 100,  # Баллы за 2 экзамен

    'exam_3_name': 'Русский язык',  # Название третьего экзамен
    'exam_3_score': 100,  # Баллы за 3 экзамен

    'wish_prof': 'Безопасник'  # Желаемая профессия'
}

print(filter_wrap.get_documents(test_atr))