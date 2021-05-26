from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from authapp.models import User
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/admin.html')


# CRUD

class UserCreateView(CreateView):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admin_staff:admin_users_read')


class UserListView(ListView):
    model = User
    template_name = 'adminapp/admin-users-read.html'


class UserUpdateView(UpdateView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users_read')
    form_class = UserAdminProfileForm


class UserDeleteView(DeleteView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users_read')
