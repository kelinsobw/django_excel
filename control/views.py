
import pandas as pd
import transliterate
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from control.forms import Weighing, read_file


def save_res(request):
    name = request.POST
    print(name)
    #cosmetic_in_cab, choice_room = build_vir_cab(cabinet)
    return HttpResponse()

def build_vir_cab(cabinet):
    data_now = read_file('all')
    head = read_file('head')
    cabinet_num = 0
    for i in range(5, len(data_now[0])):
        if (transliterate.translit(((data_now[0][i]).lower().replace(" ", "")), reversed=True)) == cabinet:
            cabinet_num = i
    print(cabinet_num)
    cosmetic_in_cab = []
    for i in range(1, len(data_now)):
        if str(data_now[i][cabinet_num]) != "nan":
            cosmetic_in_cab.append((data_now[i][2], data_now[i][3], data_now[i][4], data_now[i][cabinet_num]))
    choice_room = []
    for el in range(len(head)):
        choice_room.append(
            (str(transliterate.translit(((head[el]).replace(" ", "")), reversed=True)), str(head[el])))
    return(cosmetic_in_cab, choice_room)


def cabinet_weight(request, cabinet):
    class Cabinet_weight(forms.Form):
        cosmetic_in_cab, choice_room = build_vir_cab(cabinet)
        print(cosmetic_in_cab)
        cab = forms.CharField(label='', empty_value=cabinet)

    if request.method == "POST":
        form = Cabinet_weight(request.POST, request.FILES)
        if form.is_valid():
            info_base = form.cleaned_data
            return redirect(f"/weighing/{info_base.get('p_choice_room').lower()}", {"form": form})
    else:
        form = Cabinet_weight()
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
