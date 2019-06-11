from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .forms import StudentForm
from django.shortcuts import render




def index(request):
    form = StudentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["name"])
        print(data["name"])

        new_form = form.save()

    return render(request, 'polls/index.html', locals())



