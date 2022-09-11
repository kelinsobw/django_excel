import pandas as pd
from django.shortcuts import render, redirect
from control.forms import Weighing, read_file


def weighing(request):
    if request.method == "POST":
        form = Weighing(request.POST, request.FILES)
        if form.is_valid():
            info_base = form.cleaned_data
            return redirect(f"/weighing/{info_base.get('p_choice_room')}")
    else:
        form = Weighing()
        return render(request, "control/weighing.html", {"form": form})


def home(request):
    data = read_file('all')
    return render(request, "control/home.html", {"data": data})
