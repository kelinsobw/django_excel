from django.http import HttpResponse
from django.shortcuts import render
from datetime import *
import os, openpyxl, pathlib


def read_file():
    workbook = openpyxl.load_workbook('etual.xlsx')
    list = workbook['Производство']
    data = []
    for row in list.rows:
        for cell in row:
            data.append(cell.value)
    print(data)
    return(data)


def home(request):
    data = read_file()
    return HttpResponse('<h6>'+str(data)+'</h6>')
