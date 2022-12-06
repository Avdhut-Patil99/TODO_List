from django.shortcuts import render, redirect
from.models import mytodo
from.forms import TodoForm


def home(request):
    tasks = mytodo.objects.all()
    form = TodoForm()
    if request.method =='POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        
    return render(request,'index.html',{'tasks':tasks, 'form':form})

def deleteItem(request, pk):
    task = mytodo.objects.get(id = pk)
    task.delete()
    return redirect('home')
    