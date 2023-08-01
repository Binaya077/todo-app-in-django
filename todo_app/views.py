from django.shortcuts import render
from todo_app.models import Todo
from django.http import HttpResponseRedirect

#CRUD operation

def todo_list(request):
    todos= Todo.objects.all()
    return render(
           request,
          "bootstrap/todo_list.html",
          {
           "todos":todos},
                  
            )
def todo_delete(request, pk):
    todo=Todo.objects.get(pk=pk)
    todo.delete()
    return HttpResponseRedirect("/")

def todo_create(request):
    if request.method == "GET":
        return render(request, "bootstrap/todo_create.html")
    else:
       title= request.POST["title"]
       Todo.objects.create(title=title)
       return HttpResponseRedirect("/") #goto home page
    
def todo_update(request, pk):
    todo=Todo.objects.get(pk=pk)
    if request.method=="GET":
        return render(request, "bootstrap/todo_update.html", {"todo":todo})
    else:
        todo.title=request.POST["title"]
        todo.save()
        return HttpResponseRedirect("/") #goto homepage