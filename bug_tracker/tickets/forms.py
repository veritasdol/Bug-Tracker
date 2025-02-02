from django import forms
from .models import Ticket
from users.models import User

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'priority', 'status', 'assigned_to']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        self.fields['assigned_to'].queryset = User.objects.filter(company=user.company)
        