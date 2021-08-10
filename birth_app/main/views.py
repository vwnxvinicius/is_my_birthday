from django.forms.forms import Form
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect

# Create your views here.


class BirthDate(forms.Form):
    day = forms.IntegerField(label="Your birth day", min_value=1, max_value=31)

def get_day(request):
    if request.method == 'POST':
        form = BirthDate(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('')
    else:
        form = BirthDate()
    return render(request, "birth/index.html", {"form": form})

def home(request):
    return render(request, "birth/home.html")