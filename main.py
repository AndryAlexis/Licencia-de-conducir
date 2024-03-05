from app.routes import routes
import flet as ft

from app.ai.trainedai import DriversExamination

KEY = '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'
question = 'Cuando está intentando entrar a la autopista, debe conducir:'
short_answer = 'A la misma o casi la misma velocidad que el tráfico en la autopista.'
long_answer = 'Cuando se incorpore a una autopista, usted debe entrar a la velocidad del tránsito, o cerca de ella.'

trained_ai = DriversExamination(api_key=KEY)
response = trained_ai.send_message(question=question,
                                   short_answer=short_answer,
                                   long_answer=long_answer)

if (response is None):
    print('ALGO HA PASAO')
    exit()

print(response)
# print(response['question'], end='\n\n')
# print('\t',response['answers'][0]['text'], response['answers'][0]['isCorrect'])
# print('\t',response['answers'][1]['text'], response['answers'][1]['isCorrect'])
# print('\t',response['answers'][2]['text'], response['answers'][2]['isCorrect'])
# print('\t',response['answers'][3]['text'], response['answers'][3]['isCorrect'])
# print('\n')

# if __name__ == '__main__':
#     ft.app(target=routes, view=ft.AppView.WEB_BROWSER)