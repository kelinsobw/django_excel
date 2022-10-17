import pandas as pd
import pytils
from django import forms
from django.http import request


def transliterate_def(str_obj):
    return pytils.translit.translify(str_obj).lower().replace(" ", "")


def read_file(setting):
    data = pd.read_excel('etual.xlsx', sheet_name='Производство')
    head = data.columns.ravel()
    data = data.values.tolist()
    if setting == 'masters':
        data = pd.read_excel('etual.xlsx', sheet_name='Мастера')
        head = data.columns.ravel()
        data = data.values.tolist()
        master = []
        for i in range(1, len(data)):
            if str(data[i]) != 'nan':
                master.append(data[i][1])
            else:
                break
        data = master
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
    if setting == 'brands':
        temp = []
        for el in range(0, len(data)):
            temp.append((data[el][2], data[el][3]))
        data = temp
    return(data)



class Weighing(forms.Form):
    head = read_file('head')
    choice_room = []
    for el in range(len(head)):
        choice_room.append((str(transliterate_def(head[el])), str(head[el])))
    p_choice_room = forms.ChoiceField(choices=choice_room, label='')
    masters = read_file('masters')
    choice_master = []
    for el in range(len(masters)):
        choice_master.append((str(transliterate_def(masters[el])), str(masters[el])))
    choice_master = forms.ChoiceField(choices=choice_master, label='')
