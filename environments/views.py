""" Run Imports """
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Environments
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView



# env = [
#     {
#         'Date_Dreated': '12/28/2020',
#         'Name':'Data Solution',
#         'Description': 'This is a data management system, inteded to project and assist the teams with available information to them',
#         'Env_Stage':'Development',
#         'Platform': 'Linux',
#         'Database': 'Myslq',
#         'Run_Stack': 'Python-Django',
#         'WebServer': 'Django',
#         'IP': '10.245.100.103',
#         'Hardware': 'DELL Blade Server',
#         'ProductApp': 'SB_DataSolution',
#         'Provider': 'SB-Internal Dev',
#         'Port': '8003',
#         'Created_By': 'Teodorico Mazivila'


#     },
#     {
#         'Date_Dreated': '12/27/2020',
#         'Name':'Data Solution - Information',
#         'Description': 'This is a data management system, inteded to project and assist the teams with available information to them',
#         'Env_Stage':'Development',
#         'Platform': 'Linux',
#         'Database': 'Myslq',
#         'Run_Stack': 'Python-Django',
#         'WebServer': 'Django',
#         'IP': '10.245.100.103',
#         'Hardware': 'DELL Blade Server',
#         'Product-App': 'SB_DataSolution',
#         'Provider': 'SB-Internal Dev',
#         'Port': '8003',
#         'Created_By': 'Teodorico Mazivila'


#     },
#     {
#         'Date_Dreated': '12/28/2020',
#         'Name':'Data Solution - Documentation',
#         'Description': 'This is a data management system, inteded to project and assist the teams with available information to them',
#         'Env_Stage':'Development',
#         'Platform': 'Linux',
#         'Database': 'Myslq',
#         'Run_Stack': 'Python-Django',
#         'WebServer': 'Django',
#         'IP': '10.245.100.103',
#         'Hardware': 'DELL Blade Server',
#         'ProductApp': 'SB_DataSolution',
#         'Provider': 'SB-Internal Dev',
#         'Port': '8003',
#         'Created_By': 'Teodorico Mazivila'


#     }
# ]

# Create your views here.
def home(request):
    """ Home View"""
    context = {
        'env': Environments.objects.all()
    }
    return render(request, 'environments/home.html', context)

class EnvListView(ListView):
    """ ENV Detail View """
    model = Environments
    template_name = 'environments/home.html'
    context_object_name = 'env'
    ordering = ['-date_created']
    paginate_by = 5


class UserEnvView(ListView):
    """ User View """
    model = Environments
    template_name = 'environments/user_env.html'
    context_object_name = 'env'
    ordering = ['-date_created']
    paginate_by = 5

    def get_queryset(self):
        """ Query Set """
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Environments.objects.filter(author=user).order_by('-date_created')

class EnvDetailView(DetailView):
    """ Detail View """
    model = Environments


class EnvCreateView(LoginRequiredMixin, CreateView):
    """ Create View """
    model = Environments
    fields = [
        'date_created','name','description','env_stage', 'platform',
        'database', 'run_stack', 'web_server', 'ip', 'hardware', 'product_app',
        'port', 'provider', 'created_by' ,'status'
    ]
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EnvUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Update View """
    model = Environments
    fields = [
        'date_created','name','description','env_stage', 'platform',
        'database', 'run_stack', 'web_server', 'ip', 'hardware', 'product_app',
        'port', 'provider', 'created_by' ,'status'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        env = self.get_object()
        if self.request.user == env.author:
            return True
        return False

class EnvDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Delete View """
    model = Environments
    success_url = '/'

    def test_func(self):
        env = self.get_object()
        if self.request.user == env.author:
            return True
        return False

def about(request):
    """ About Page """
    return render(request, 'environments/about.html', {'title': 'About'})
