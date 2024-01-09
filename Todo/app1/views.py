from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,redirect
from .models import Todo

# Create your views here.
def home(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        list = Todo(t_title=title,t_description=description)
        list.save()
    return render(request,'home.html')

def list(request):
    if request.method == 'GET':
        a = Todo.objects.all()
        return render(request,'tasklist.html',{'list':a})
    
def Update_Task(request):
    if request.method == 'POST':

        id = request.POST['id']
        title = request.POST['title']
        description = request.POST['description']
        
        b = get_object_or_404(Todo,pk=id)
        
        b.t_title=title
        b.t_description = description
        b.save()
        return HttpResponseRedirect ("/list/")
    
def Delete_Task(request,id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/list/')