from django.shortcuts import redirect, render
#from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm 
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from trello_app.models import task, task_list
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method=='POST':
        form=CreateUserForm(data=request.POST) 
        if form.is_valid():
            form.save()

    else:
        form=CreateUserForm()

    return render(request,'pages/register.html', {'form':form})
    

def logout(request):
    auth_logout(request)
    return redirect('home')


@login_required(login_url='login')
def dashboard(request):
    user=request.user
    lists=task_list.objects.filter(user=user)
    tasks=task.objects.filter(list__in=lists)
    return render(request,'pages/dashboard.html',{'lists':lists,'tasks':tasks})
    # if request.method=='POST':
    #     auth_logout(request)
    #     return redirect('login')
    # return render(request,'pages/dashboard.html')


def login(request):
    if request.method=='POST':
        #if the user exists with given credentials
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request,user)
            #redirect to dashboard
            return redirect('dashboard')
        else:
            #provide some error messages here
            messages.error(request,'Username or password is incorrect')
    return render(request,'pages/login.html')

def home(request):
    if request.user.is_authenticated:
        #if the user is logged in
        return redirect('dashboard')
    return render(request, 'pages/home.html')