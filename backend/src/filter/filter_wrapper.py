import pandas as pd
import json


class FilterWrapper:
    def __init__(self, data_url, profs_url):
        self.df = pd.read_csv(data_url)
        self.profs = pd.read_csv(profs_url)

        self.df['Направление'] = self.df['Направление'].apply(
            lambda x: ' '.join(x.split(' ')[1:])  # Убираем дату из названия направления
        )

    def get_documents(self, abiture_data):
        exams, wish_prof = self.__parse_data(abiture_data)

        filtered_df = self.df.copy()
        for subject, score in exams:
            filtered_df = (
                filtered_df[
                    ((filtered_df['Мин. балл 1'] <= score) & (filtered_df['Предмет 1'] == subject)) |
                    ((filtered_df['Мин. балл 2'] <= score) & (filtered_df['Предмет 2'] == subject)) |
                    ((filtered_df['Мин. балл 3'] <= score) & (filtered_df['Предмет 3'] == subject))
                ]
            )

        filtered_df = self.__rank(filtered_df, wish_prof)

        json_response = json.loads(filtered_df.to_json(orient='index', force_ascii=False))

        return json_response

    def __parse_data(self, abiture_data):
        exams = [
            (subject, score) for subject, score in zip(
                abiture_data['subjects'], abiture_data['scores']
            )
        ]

        wish_prof = abiture_data['profession']
        return exams, wish_prof

    def __rank(self, df, wish_prof):
        #print(self.profs)
        wished_profs = self.profs[self.profs['Профессия'] == wish_prof]
        #print('Программная инженерия' in wished_profs['Конкурсн. группа'].values)

        df['wished'] = df['Конкурсн. группа'].apply(
            lambda x: (
                True
                if x in wished_profs['Конкурсн. группа'].values else
                False
            )
        )

        return df.sort_values(by=['wished'], ascending=False)



