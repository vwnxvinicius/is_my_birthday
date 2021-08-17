from django import forms
from django.http.response import ResponseHeaders
from django.shortcuts import render
from django.http import HttpResponseRedirect, request
from django.urls import reverse
import datetime


# Create your views here.
now = datetime.datetime.now()
day = str(now.day)
month = str(now.month)



def result(request):
    return render(request, "birth/result.html")


def isnt_birth(request):
    return render(request, "birth/notbirth.html")


class BirthDate(forms.Form):
    dia = forms.IntegerField( min_value=1, max_value=31)
    mes = forms.IntegerField(min_value=1, max_value=12)

def home(request):
    if request == "POST":
        form = BirthDate(request.POST)
        if form.is_valid():
            dia = form.cleaned_data["dia"]
            mes = form.cleaned_data["mes"]
    else:
        return render(request, "birth/home.html",{
        "form": BirthDate()
        })
        
    return render(request, "birth/home.html",{
        "form": BirthDate(),
        "day": request.POST.get("dia") == day,
        "month": request.POST.get("mes") == month,
        })
def is_birth(request):
    return render(request, "birth/isbirth.html",{
        "day": request.POST.get("dia") == day,
        "month": request.POST.get("mes") == month,
    })
