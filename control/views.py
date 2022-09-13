
import pandas as pd
import transliterate
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from control.forms import Weighing, read_file


def cabinet_weight(request, cabinet):
    class Cabinet_weight(forms.Form):
        data_now = read_file('all')
        head = read_file('head')
        cabinet_num = 0
        weight_info = []
        counter = [0, 1, 2, 3]
        for i in range(5, len(data_now[0])):
            if (transliterate.translit(((data_now[0][i]).lower().replace(" ", "")), reversed=True)) == cabinet:
                cabinet_num = i
        cosmetic_in_cab = []
        for i in range(1,len(data_now)):
            if str(data_now[i][cabinet_num]) != "nan":
                cosmetic_in_cab.append((data_now[i][2],data_now[i][3],data_now[i][4],data_now[i][cabinet_num]))
        choice_room = []
        for el in range(len(head)):
            choice_room.append(
                (str(transliterate.translit(((head[el]).replace(" ", "")), reversed=True)), str(head[el])))
        p_choice_room = forms.ChoiceField(choices=choice_room, label='')

    if request.POST:
        if '_formi' in request.POST:
            print(("as________________as"))

    if request.method == "POST":
        form = Cabinet_weight(request.POST, request.FILES)
        if form.is_valid():
            print("qwerty")
            print(form.cleaned_data)
            info_base = form.cleaned_data
            return redirect(f"/weighing/{info_base.get('p_choice_room').lower()}", {"form": form})
    else:
        form = Cabinet_weight()
        print("jskd")
        return render(request, "control/cabinet_weight.html", {"form": form})


def weighing(request):
    if request.method == "POST":
        form = Weighing(request.POST, request.FILES)
        if form.is_valid():
            info_base = form.cleaned_data
            return redirect(f"/weighing/{info_base.get('p_choice_room').lower()}")
    else:
        form = Weighing()
        return render(request, "control/weighing.html", {"form": form})


def home(request):
    data = read_file('all')
    return render(request, "control/home.html", {"data": data})
