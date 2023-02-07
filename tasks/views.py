from django import forms
from django.shortcuts import render, redirect

# Create your views here.

tasks = []
names = []
class NewTaskForm(forms.Form):
    task = forms.CharField(label="Task")
    name = forms.CharField(label="names")


def index(request):
    context = {"names": names,"tasks":tasks}
    return render(request, "tasks/index.html", context)


def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            name = form.cleaned_data["name"]
            names.append(name)
            return redirect("tasks:index")
        else:
            return render(request, "tasks/add.html", {"form":form})
            
    return render(request, "tasks/add.html", {"form":NewTaskForm})