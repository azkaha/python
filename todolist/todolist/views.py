from django.shortcuts import render, get_object_or_404
from .models import Todo

def index(request):  # home page
    query = request.GET.get('q')  # get the search query from the request
    if query: # not empty
        todos = Todo.objects.filter(tasktodo__icontains=query).order_by('-created_at')  # filter todos based on search query
    else:
        todos = Todo.objects.all().order_by('-created_at')  # get all the todos and order by newest first
    return render(request, 'index.html', {'todos': todos, 'query': query})  # passing the list of todos and the query back to the template
# basically if query is empty itll render all the todos otherwise only the imp todos in home

def create_todo(request):  # creating a new to-do
    if request.method == 'POST': # theres GET or POST we use POST bcs submitting data to server
        tasktodo = request.POST.get('tasktodo') #get tasktodo from it
        if tasktodo:  # if its not empty
            Todo.objects.create(tasktodo=tasktodo) # create a new object and saved it to the database
    todos = Todo.objects.all().order_by('-created_at')  # get all the todos and order by newest first  
    return render(request, 'todo-list.html', {'todos': todos})

def mark_todo(request, pk):  # changing completed to true
    todo = get_object_or_404(Todo, pk=pk) # Get object with the given primary key or return a 404 if not found
    todo.ifcompleted = True
    todo.save() # save to the database
    todos = Todo.objects.all().order_by('-created_at')  # get all the todos and order by newest first  
    return render(request, 'todo-list.html', {'todos': todos})  # render 'todo-list.html' with updated todos


def delete_todo(request, pk):  # deleting a to-do
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    todos = Todo.objects.all().order_by('-created_at')  # get all the todos and order by newest first
    return render(request, 'todo-list.html', {'todos': todos}) # render 'todo-list.html' with updated todos