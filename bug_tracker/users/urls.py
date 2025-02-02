from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view, logout_view, users_list_view, add_user_view, delete_user_view


urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', logout_view, name='logout'),
    path('', users_list_view, name='users_list'),
    path('add/', add_user_view, name='add_user'),
    path('delete/<int:user_id>/', delete_user_view, name='delete_user'),

]