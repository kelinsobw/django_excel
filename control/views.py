import openpyxl
import transliterate
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from control.forms import Weighing, read_file


def save_res(request, cabinet, master):
    return HttpResponse("Ju")


def start_otchet(name, master, my_data):
    '''workbook_temp = openpyxl.load_workbook('shablon.xlsx')
    data = workbook_temp["Шаблон"]'''
    my_data = list(my_data.items())
    row = 7
    itog = 0
    otchet = []
    itog_brand = 0
    m = read_file('masters')
    n = read_file('head')
    for i in (0, len(m)-1):
        if transliterate.translit(m[i].lower().replace(" ", ""), reversed=True) == master:
            master = m[i]
    for i in (0, len(n)-1):
        if transliterate.translit(n[i].lower().replace(" ", ""), reversed=True) == name:
            name = n[i]
    '''    data['B4'] = master
    data['B2'] = name'''
    old_info, non = build_vir_cab(name, 1)
    del my_data[0]
    for i in range(0, len(old_info)-1):
        print(my_data[i][1])
        if str(my_data[i][1]) != '':
            print("+++")
            otchet.append([old_info[i][0], old_info[i][1], float(old_info[i][3])-float(my_data[i][1]), float(old_info[i][4])*(float(old_info[i][3])-float(my_data[i][1]))])
    print(otchet)

def write_in_excel(name, master, my_data):
    start_otchet(name,master,my_data)
    '''cosmetic_in_cab, choice_room = build_vir_cab(name)
    my_data = list(my_data.items())
    del my_data[0]
    write_otchet = []
    for i in range(len(cosmetic_in_cab)):
        print(cosmetic_in_cab[i][3])
    for i in range(len(my_data)):
        print(my_data[i][1])
    for i in range(len(cosmetic_in_cab)):
        if str(my_data[i][1]) != '':
            write_otchet.append((cosmetic_in_cab[i][0],
                                 cosmetic_in_cab[i][1],
                                 (float(cosmetic_in_cab[i][3])-float(my_data[i][1]))))

    workbook_temp = openpyxl.load_workbook('etual.xlsx')
    data = workbook_temp["Производство"]
    simvols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    coord = None
    for i in range(4, 1000):
        if transliterate.translit(data[str(simvols[i]) + '1'].value.lower().replace(" ", ""), reversed=True) == name:
            coord = simvols[i]
            break
    for j in range(0, len(cosmetic_in_cab)):
        for i in range(1, 1000):
            if cosmetic_in_cab[j][1] == data['D'+str(i)].value:
                if str(my_data[j][1]) != '0':
                    data[coord + str(i)] = (my_data[j][1])
    workbook_temp.save('etual.xlsx')'''


def build_vir_cab(cabinet, setting=0): #setting == 0=>don't price, 1>price
    data_now = read_file('all')
    head = read_file('head')
    cabinet_num = 0
    for i in range(5, len(data_now[0])):
        if (transliterate.translit(((data_now[0][i]).lower().replace(" ", "")), reversed=True)) == cabinet:
            cabinet_num = i
    cosmetic_in_cab = []
    for i in range(1, len(data_now)):
        if str(data_now[i][cabinet_num]) != "nan":
            if str(setting) == "1":
                cosmetic_in_cab.append((data_now[i][2], data_now[i][3], data_now[i][4], data_now[i][cabinet_num], data_now[i][6]/data_now[i][4]))
            else:
                cosmetic_in_cab.append((data_now[i][2], data_now[i][3], data_now[i][4], data_now[i][cabinet_num]))
    choice_room = []
    for el in range(len(head)):
        choice_room.append(
            (str(transliterate.translit(((head[el]).replace(" ", "")), reversed=True)), str(head[el])))
    return(cosmetic_in_cab, choice_room)


def cabinet_weight(request, cabinet, master):
    class Cabinet_weight(forms.Form):
        cosmetic_in_cab, choice_room = build_vir_cab(cabinet)
        x = str(request.build_absolute_uri())
        x = x[x.rindex("/") + 1:]

    name = str(request.build_absolute_uri())
    name = name.replace("/", " ")
    name = name.split()
    master = str(name[-1])
    name = str(name[-2])
    if request.method == "POST":
        form = Cabinet_weight(request.POST, request.FILES)
        if form.is_valid():
            data = request.POST
            write_in_excel(name, master, data)
            return redirect(f"/weighing/{str(name)}/save_res", {"form": form})
    else:
        form = Cabinet_weight()
        return render(request, "control/cabinet_weight.html", {"form": form})


def weighing(request):
    if request.method == "POST":
        form = Weighing(request.POST, request.FILES)
        if form.is_valid():
            info_base = form.cleaned_data
            return redirect(f"/weighing/{info_base.get('p_choice_room').lower()}/{info_base.get('choice_master').lower()}")
    else:
        form = Weighing()
        return render(request, "control/weighing.html", {"form": form})


def home(request):
    data = read_file('all')
    return render(request, "control/home.html", {"data": data})
