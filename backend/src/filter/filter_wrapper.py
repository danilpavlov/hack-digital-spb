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

        for i in range(1, 4):
            subject_col = f'Предмет {i}'
            score_col = f'Мин. балл {i}'

            # Filter rows where the subject is in the exams keys
            filtered_df = filtered_df[filtered_df[subject_col].isin(exams.keys())]

            # Apply condition to drop rows where the score is greater than the corresponding score in exams
            filtered_df = filtered_df[~(filtered_df[score_col] > filtered_df[subject_col].map(exams))]

        filtered_df = self.__rank(filtered_df, wish_prof)

        json_response = json.loads(filtered_df.to_json(orient='index', force_ascii=False))

        return json_response

    def __parse_data(self, abiture_data):
        exams = {
            subject: score for subject, score in zip(
                abiture_data['subjects'], abiture_data['scores']
            )
        }

        wish_prof = abiture_data['profession']
        return exams, wish_prof

    def __rank(self, df, wish_profs):
        wished_profs = self.profs[self.profs['Профессия'].isin(wish_profs)]

        df['wished'] = df['Конкурсн. группа'].apply(
            lambda x: (
                True
                if x in wished_profs['Конкурсн. группа'].values else
                False
            )
        )

        return df.sort_values(by=['wished'], ascending=False).copy()