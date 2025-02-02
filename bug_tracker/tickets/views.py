from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import TicketForm
from users.decorators import role_required


@login_required
@role_required(allowed_roles=['admin', 'tester'])
def create_ticket_view(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_by = request.user
            ticket.company = request.user.company
            ticket.save()
            return redirect('ticket_list')
    else:
        form = TicketForm()
    return render(request, "tickets/ticket_form.html", {"form": form})

@login_required
def ticket_list_view(request):
    
    if request.user.role == "admin":
        tickets = Ticket.objects.filter(company=request.user.company)
    elif request.user.role == "tester":
        tickets = Ticket.objects.filter(company=request.user.company, created_by=request.user)
    elif request.user.role == "developer":
        tickets = Ticket.objects.filter(company=request.user.company, assigned_to=request.user)
    return render(request, "tickets/ticket_list.html", {"tickets": tickets})

@login_required
@role_required(allowed_roles=['admin', 'developer'])
def update_ticket_view(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, company=request.user.company)
    if request.method == "POST":
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            ticket = form.save()
            return redirect('ticket_list')
    else:
        form = TicketForm(instance=ticket)
    return render(request, "tickets/ticket_form.html", {"form": form})

@login_required
@role_required(allowed_roles=['admin'])
def delete_ticket_view(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, company=request.user.company)

    if request.method == "POST":
        ticket.delete()
        return redirect('ticket_list')
    return render(request, "tickets/ticket_confirm_delete.html", {"ticket": ticket})