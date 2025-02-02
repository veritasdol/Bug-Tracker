from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, AddUserForm
from .decorators import role_required
from .models import User

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
@role_required("admin")
def users_list_view(request):
    users = User.objects.filter(company=request.user.company)
    return render(request, "users/users_list.html", {"users": users})

@login_required
@role_required("admin")
def add_user_view(request):
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save(admin_user=request.user)
            return redirect('users_list')
    else:
        form = AddUserForm()
    return render(request, "users/add_user.html", {"form": form})


@login_required
@role_required("admin")
def delete_user_view(request, user_id):

    user = get_object_or_404(User, id=user_id, company=request.user.company)
    if request.method == "POST":
        user.delete()
        return redirect('users_list')