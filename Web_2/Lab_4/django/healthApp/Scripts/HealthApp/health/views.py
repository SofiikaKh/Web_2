from django.shortcuts import render, redirect
import requests
from .models import Symp
from .forms import SympForm, CreateUserForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
    url = "https://sandbox-healthservice.priaid.ch/diagnosis?symptoms=[{}]&gender=female&year_of_birth=40&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InNvZmlpa2E3QGdtYWlsLmNvbSIsInJvbGUiOiJVc2VyIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvc2lkIjoiODIxMiIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvdmVyc2lvbiI6IjIwMCIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGltaXQiOiI5OTk5OTk5OTkiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXAiOiJQcmVtaXVtIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9sYW5ndWFnZSI6ImVuLWdiIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9leHBpcmF0aW9uIjoiMjA5OS0xMi0zMSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcHN0YXJ0IjoiMjAyMC0xMS0yNiIsImlzcyI6Imh0dHBzOi8vc2FuZGJveC1hdXRoc2VydmljZS5wcmlhaWQuY2giLCJhdWQiOiJodHRwczovL2hlYWx0aHNlcnZpY2UucHJpYWlkLmNoIiwiZXhwIjoxNjA3MDMxNjkyLCJuYmYiOjE2MDcwMjQ0OTJ9.VAaT-9RRGtFqkmllc_j1ynSfiwwdb3Fo6E8yp748boQ&format=json&language=ru-ru"
    listD=[]
    
    if(request.method == "POST"):
         form= SympForm(request.POST)
         form.save()


    form=  SympForm()  

    symptomIDs=Symp.objects.all()

    all_symp=[]

    for sId in symptomIDs:
        response = requests.get(url.format(sId.name))
        res=response.json()
        
        for i in range(len(res)):
            listD.append(res[i]["Issue"]["Name"])
        diag_info = {
            'symptomID': sId.name,
            'issue':  listD,
        }
        all_symp.append(diag_info)
    
    context = {'all_info': all_symp, 'form':form}
    Symp.objects.all().delete()
    return render(request, 'health/index.html',context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user= form.cleaned_data.get('username')

                messages.success(request, 'Account was created successfully for ' + user)
                return redirect('login')


        context={'form':form}
        return render(request, 'health/register.html',context)
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR Password is incorrect')

        context={}
        return render(request, 'health/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def listt(request):
    return redirect('list')