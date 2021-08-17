from django.shortcuts import render
# from . import views
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import TaskForm, MapsForm
from .models import Task3
from .phones import extract_phones

from .manager import compute
import json



# нужно загружать данные в джангу из джаваскрипта как-то
# настроить пайплайн для расчета а там ещё кусок базы данных кстати. взять элемент, обновить элемент
# написать больше текста в дисер
# улучшить презентацию
# запуск или не запуск на ноуте?











# Create your views here.

def mainPage(request):
    error = "_"
    if request.method=="POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            # form.save()
            # redirect("home")
            theText = str(form.data["Title"])
            preNum = str(form.data["stNumber"])
            endNum = str(form.data["ndNumber"])
            error = extract_phones(theText, preNum, endNum)
        else:
            error = 'Wrong'

    form = TaskForm()
    contexte = {
        "Title":"Phones from text extractor + reformater",
        "additional_content":form,
        'error': error
    }
    return render(request, "main/additionak.html",contexte)# {"Title":"Phones from text extractor + reformater","additional_content":"additional_content"} )#context)




def mapPage(request):
    returnToUser = "_"
    if request.method=="POST":
        # updatedData = json.loads(request.body.decode('UTF-8'))
        # print(updatedData)
        form = MapsForm(request.POST)
        if form.is_valid():

            listOfPoints= str(form.data["Field1"])
            param1= str(form.data["Field1"])
            param2= str(form.data["Field2"])
            param3= str(form.data["Field3"])
            # theText = str(form.data["Title"])
            # preNum = str(form.data["stNumber"])
            # endNum = str(form.data["ndNumber"])


            returnToUser = compute(listOfPoints, param1,param2,param3)
        else:
            returnToUser = 'Wrong'

    form = MapsForm()
    contexte = {
        "Title":"MapsCalculator",
         "additional_content":form,
        'returnToUser': returnToUser
    }
    return render(request, "main/forMapPage.html",contexte)# {"Title":"Phones from text extractor + reformater","additional_content":"additional_content"} )#context)

