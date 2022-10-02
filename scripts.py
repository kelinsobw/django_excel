'''kosmeticheskijbeauty
Косметический beauty'''
import pandas as pd


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
        for el in range(1, len(data)):
            temp.append(data[el][1], data[el][2])
        data = temp
    return(data)

print(read_file("brands"))