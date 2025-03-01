from django.shortcuts import render
from django.views import View
from .models import Todo
from .mixins import TodoMixin
from .forms import TodoForm

class IndexView(View):
    def get(self, request):
        return render(request, 'Home/index.html')


class TodoListView(View):
    def get(self, request):
        todos = Todo.objects.filter(user = request.user)
        return render(request, 'Home/todo_list.html', {'todos': todos})


class TodoDetailView(TodoMixin, View):
    template_name = 'Home/todo_detail.html'


