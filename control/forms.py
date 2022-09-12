import pandas as pd
from django import forms
import transliterate



def read_file(setting):
    data = pd.read_excel('etual.xlsx', sheet_name='Производство')
    head = data.columns.ravel()
    data = data.values.tolist()
    if setting == 'all':
        temp = [head]
        for el in data:
            temp.append(el)
        data = temp
    if setting == 'head':
        data = []
        for el in range(9, len(head)):
            data.append(head[el])
    if setting == 'data':
        temp = []
        for el in range(len(data)):
            temp.append(data[el])
        data = temp
    return(data)


class Weighing(forms.Form):
    head = read_file('head')
    choice_room = []
    for el in range(len(head)):
        choice_room.append((str(transliterate.translit(((head[el]).replace(" ", "")), reversed=True)), str(head[el])))
    p_choice_room = forms.ChoiceField(choices=choice_room, label='')


