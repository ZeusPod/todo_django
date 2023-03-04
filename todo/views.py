from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import Task
from .forms import TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomeView(LoginRequiredMixin,generic.TemplateView):
    template_name = 'home.html'
    login_url = 'todo:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = Task.objects.filter(user = self.request.user)
        return context
    


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('home')
    template_name = 'home.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('todo:home')
    


class DeleteTaskView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy('todo:home')
    
    

class UpdateTaskView(generic.UpdateView):
    model = Task
    fields = ['title','description', 'limite_date', 'status', 'color']
    success_url = reverse_lazy('todo:home')



    def form_valid(self, form):
        return super().form_valid(form)
    


    def form_invalid(self, form):
        return super().form_invalid(form)