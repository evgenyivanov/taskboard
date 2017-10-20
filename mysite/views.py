import datetime
from operator import itemgetter
from io import TextIOWrapper
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
#from django.forms.util import ErrorList
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from mysite.models import *
from mysite.forms import *

###############################################################################
@csrf_protect
def login2(request):
    if request.method == 'POST':
        f = LoginForm(request.POST)
        login_ = User.objects.filter(pk = request.POST['login'])[0]

        password = request.POST['password']
        user = authenticate(username=login_, password=password)
        if  user is not None:
            login(request, user)
            return redirect('/')
        else:
            d = {'f': f,'errors':'Error: login and password'}

            return render(request, "login.html", d)
    else:
       f = LoginForm
       d = {'f': f}

       return render(request, "login.html", d)

@csrf_protect
@login_required
def taskedite(request,id=''):

    if request.method == 'GET':
        attachs = []
        author = ''


        if id != '':
            obj = Tasks.objects.get(pk=id)
            numer = obj.id
            author = str(obj.user)
            form = TaskForm(instance=obj)
            files= Files.objects.filter(task = obj)
            number=0
            for i in files:

                attachs.append(str(i.id))
        else:
            numer = ''
            form = TaskForm({'user':request.user,'start':datetime.datetime.now()})

        d = {'f': form,'attachs':attachs,'author':author,'id':numer}


        return render(request, "editetask.html", d)

    elif request.method == "POST":
        attachs = []
        if id != '':
            obj = Tasks.objects.get(pk=id)
            numer = obj.id
            author = obj.user
            form = TaskForm(request.POST,instance = obj)
            files= Files.objects.filter(task = obj)
            number=0
            for i in files:
                number = number +1
                attachs.append(str(numer))
        else:
            numer = ""
            form = TaskForm(request.POST)
            form.user = request.user

        if not form.is_valid():
            d = {'f': form,'errors':form.errors,'attachs':attachs,'author':author,'id':numer}
            return render(request, "editetask.html", d)
        else:
            result = form.save()



            if 'file' in request.FILES:

                new_file = Files()
                new_file.task = result
                new_file.data = request.FILES['file']
                new_file.save()
            return redirect('/')

@login_required
def imgview(request,id):
    obj = Files.objects.filter(id = id)[0]
    result = '<img src="http://oskolki1.pythonanywhere.com/'+obj.data.url+'"  weght = 75% height = 75%>'
    return HttpResponse(result)

@csrf_protect
@login_required
def main(request):
    curent_profile = Profile.objects.filter(user = request.user)[0]
    f = MainForm({'status':curent_profile.status,'start':curent_profile.start,'finish':curent_profile.finish})
    d = {'f':f, 'user':request.user}
    return render(request, "main.html", d)


@csrf_protect
@login_required
def tasklist(request,status,start_month,start_day,start_year,finish_month,finish_day,finish_year):
    curent_status = StatusOfTasks.objects.filter(id = status)[0]
    start = datetime.datetime(int(start_year), int(start_month), int(start_day), 0, 0)
    finish = datetime.datetime(int(finish_year), int(finish_month), int(finish_day), 23, 59)
    curent_profile = Profile.objects.filter(user = request.user)[0]
    curent_profile.status = curent_status
    curent_profile.start = start
    curent_profile.finish = finish
    curent_profile.save()



    if Profile.objects.filter(user = request.user)[0].user_type == 1:
        L = Tasks.objects.filter(status = curent_status).filter(start__gte = start).filter(start__lte = finish)

    else:
        L=Tasks.objects.filter(user = request.user).filter(status = curent_status).filter(start__gte = start).filter(start__lte = finish)


    L.filter(status = curent_status)

    d = {'L':L}
    return render(request, "task_list.html", d)


