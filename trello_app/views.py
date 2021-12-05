from django.shortcuts import redirect, render
from .models import task_list, task
from .forms import task_form
from django.contrib.auth.decorators import login_required
def index(request):
    #this data is coming now from the database
    lists=task_list.objects.all()
    tasks=task.objects.all()
    return render(request, 'trello_app/index.html',{'lists':lists , 'tasks':tasks})
# Create your views here.
@login_required(login_url='login')
def create_list(request):
    if request.method=='POST':
        l_name=request.POST['list_name']
        list=task_list(name=l_name,user=request.user)
        list.save()
        return redirect('home')
    else:
        return render(request,'trello_app/new_list.html')
        
@login_required(login_url='login')
def create_task(request):
    if request.method=='POST':
        form=task_form(data=request.POST)
        form.instance.user=request.user
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form=task_form
        return render(request,'trello_app/new_task.html',{'form':form})