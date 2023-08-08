from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from .forms import TodoForm
from .models import Todo

class TodoMixin:
    form_class = TodoForm
    template_name = None

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            todo = get_object_or_404(Todo, id=kwargs['pk'])
            if not todo.user == request.user:
                raise PermissionDenied
            return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, pk):
        todo = Todo.objects.filter(id=pk)
        form = self.form_class()
        context = {
            'todo': todo,
            'form': form,
            }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        todo = Todo.objects.get(id=pk)
        form = self.form_class(request.POST, instance=todo)
        if form.is_valid():
            todo.save()
            return redirect('thank_you')
        return render(request, self.template_name, {'todo': todo})
