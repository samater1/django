from django import forms
from django.shortcuts import render, redirect

# Create your views here.
class NewTaskForm(forms.Form):
    task = forms.CharField(label="Task")


def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    context = {"tasks":request.session["tasks"]}
    return render(request, "tasks/index.html", context)


def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return redirect("tasks:index")
        else:
            return render(request, "tasks/add.html", {"form":form})
            
    return render(request, "tasks/add.html", {"form":NewTaskForm})