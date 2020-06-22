from django.shortcuts import render,redirect
from .models import TodoModel
# Create your views here.


def todoview(request):
    mytodos = TodoModel.objects.all()
    context = {'mytodos' : mytodos}
    return render(request,"todoapp/homepage.html",context)


def addtask(request):
    mytask = request.POST['task']
    TodoModel(task = mytask).save()
    return redirect(request.META['HTTP_REFERER'])


def deletetask(request,taskpk):
    TodoModel.objects.filter(id = taskpk).delete()
    return redirect(request.META['HTTP_REFERER'])


def edittaskview(request,taskpk):
    context={'todopk' : taskpk}
    return render(request,"todoapp/edittask.html",context)


def edittask(request,taskpk):
    newtask = request.POST['task']
    todo = TodoModel.objects.filter(id = taskpk)[0]
    todo.task = newtask
    todo.save()
    return redirect('homepage')