from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

# Create your views here.
from django.http import HttpResponse

class TaskList(ListView):
   model = Task
   context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'handl/task_detail.html'

class TaskCreate(CreateView):
    model = Task
    fields = ['user','title','tasktype','description','repeatevent','moyval','complete']
    success_url = reverse_lazy('tasks')

   # def form_valid(self, form):
   #     form.instance.user = self.request.user
   #     return super(TaskCreate, self).form_valid(form)
class TaskUpdate(UpdateView):
    model = Task
    fields = ['title', 'description','complete']
    success_url = reverse_lazy('tasks')

class DeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')