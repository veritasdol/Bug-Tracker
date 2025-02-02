from django.urls import path
from .views import ticket_list_view, create_ticket_view, update_ticket_view, delete_ticket_view, ticket_detail_view

urlpatterns = [
    path('', ticket_list_view, name='ticket_list'),
    path('create/', create_ticket_view, name='create_ticket'),
    path('update/<int:ticket_id>/', update_ticket_view, name='update_ticket'),
    path('delete/<int:ticket_id>/', delete_ticket_view, name='delete_ticket'),
    path('ticket/<int:ticket_id>/', ticket_detail_view, name='ticket_detail'),
]