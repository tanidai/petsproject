from re import template
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login,logout
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import listtablemodel

def IndexView(request):
    listmodel = listtablemodel.objects.filter(modeltaip='譲渡前').last()
    return render(request,'index.html' ,{'listmodel':listmodel})

def loginview(request):
    if request.method =='POST':
        username_data = request.POST['Username_data']
        password_data = request.POST['password_data']
        user = authenticate(request, username=username_data,password=password_data)
        if user is not None:
            login(request, user)
            return redirect('petsgallery:index')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def signupview(request):
    if request.method =='POST':
        username_data = request.POST['Username_data']
        password_data = request.POST['password_data']
        try:
            user = User.objects.create_user(username_data, '', password_data)
            login(request, user)
            return redirect('petsgallery:index')
        except IntegrityError:
            return render(request, 'signup.html',{'error':'このユーザーは既に登録されています'})
    else:
        return render(request, 'signup.html')

def Listview(request):
    object_list = listtablemodel.objects.all().filter(modeltaip='譲渡前').order_by('-id')[:5]
    return render(request,'List.html' ,{'object_list':object_list})

def AftreListview(request):
    object_list = listtablemodel.objects.all()

    return render(request,'AfterList.html' ,{'object_list':object_list})
class Logouthtmlview(TemplateView):
    template_name = 'logout.html'
def gobackview(request):
    logout(request) 
    return redirect('petsgallery:index')

class myselfview(TemplateView):
    template_name = 'myself.html'

def photobuildingview(request):
    object_list = listtablemodel.objects.all().filter(modeltaip='譲渡後').order_by('-id')[:5]
    return render(request,'photobuilding.html' ,{'object_list':object_list})

class CreateClass(CreateView):
    template_name = 'ArticleProduction.html'
    model = listtablemodel
    fields = ('title','content','author','images1','images2','images3','evaluation','modeltaip')
    success_url = reverse_lazy('petsgallery:List')

def ArticleDetailsview(request,pk):
    object = listtablemodel.objects.get(pk=pk)
    return render(request, 'ArticleDetails.html',{'object':object})


def deletelistview(request):
    username_data = request.user.id
    object_list = listtablemodel.objects.all().filter(author=username_data).order_by('-id')
    return render(request,'deletelist.html' ,{'object_list':object_list})

def deleteview(request,pk):
    try:
        deleteblog = listtablemodel.objects.get(pk=pk)
    except listtablemodel.DoesNotExist:
        return redirect('petsgallery:deletelist')
    deleteblog.delete()
    return redirect('petsgallery:deletelist')

def choiceview(request):
    if request.method == "POST":
        choice = request.POST['jpmap']
        posted = request.POST['posted']
        object_list = listtablemodel.objects.all().filter(evaluation=choice).filter(modeltaip=posted).order_by('-id')[:5]
        return render(request,'List.html' ,{'object_list':object_list})
    else:
        return render(request,'List.html' ,{'object_list':object_list})
def choice1view(request):
    if request.method == "POST":
        choice = request.POST['jpmap']
        object_list = listtablemodel.objects.all().filter(evaluation=choice).filter(modeltaip='譲渡前').order_by('-id')[:5]
        return render(request,'List.html' ,{'object_list':object_list})
    else:
        return render(request,'List.html' ,{'object_list':object_list})