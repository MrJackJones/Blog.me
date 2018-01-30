from django.views import generic
from .models import Post, Categories
from django.views.generic.edit import UpdateView, DeleteView, CreateView, FormView
from django.views.generic.base import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


class IndexView(generic.ListView):
    template_name = 'main/index.html'
    context_object_name = 'all_post'

    def get_queryset(self):
        return Post.objects.all()


class DetailView(generic.DetailView):
    model = Post
    template_name = 'main/detail.html'


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"

    template_name = "main/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "main/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


# Представление для создания сигнатуры
class Create_post(CreateView):
    model = Post
    fields = ['title', 'image', 'post', 'categories']


# Представление для изменения сигнатуры
class Update_post(UpdateView):
    model = Post
    fields = ['title', 'image', 'post', 'categories']


# Представление для удлаения сигнатуры
class Delete_post(DeleteView):
    model = Post
    success_url = reverse_lazy('main:index')