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
        exam_scores, full_exam_score, exam_names, wish_prof = self.__parse_data(abiture_data)
        filtered_df = self.df[
            (self.df['Мин. балл 1'] <= exam_scores.get(1)) & (self.df['Предмет 1'] == exam_names.get(1)) &
            (self.df['Мин. балл 2'] <= exam_scores.get(2)) & (self.df['Предмет 2'] == exam_names.get(2)) &
            (self.df['Мин. балл 3'] <= exam_scores.get(3)) & (self.df['Предмет 3'] == exam_names.get(3))
        ].copy()

        filtered_df = self.__rank(filtered_df, wish_prof)

        json_response = json.loads(filtered_df.to_json(orient='index', force_ascii=False))

        return json_response

    def __parse_data(self, abiture_data):
        exam_scores = {
            1: abiture_data['exam_1_score'],
            2: abiture_data['exam_2_score'],
            3: abiture_data['exam_3_score'],
        }

        full_exam_score = sum(exam_scores.values())

        exam_names = {
            1: abiture_data['exam_1_name'],
            2: abiture_data['exam_2_name'],
            3: abiture_data['exam_3_name'],
        }

        wish_prof = abiture_data['wish_prof']
        return exam_scores, full_exam_score, exam_names, wish_prof

    def __rank(self, df, wish_prof):
        wished_profs = self.profs[self.profs['Профессия'] == wish_prof]

        df['wished'] = df['Конкурсн. группа'].apply(
            lambda x: (
                True
                if x in wished_profs['Конкурсн. группа'] else
                False
            )
        )

        return df.sort_values(by=['wished'], ascending=False)



