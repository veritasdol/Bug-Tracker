from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Company

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    company_name = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ["username", "email", "company_name", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        company, created = Company.objects.get_or_create(name=self.cleaned_data["company_name"])
        user.company = company
        user.role = "admin"  # The first user is always an admin
        if commit:
            user.save()
        return user
    
class AddUserForm(UserCreationForm):
    email = forms.EmailField()
    role = forms.ChoiceField(choices=[("developer", "Developer"), ("tester", "Tester")])

    class Meta:
        model = User
        fields = ["username", "email", "role", "password1", "password2"]

    def save(self, admin_user, commit=True):
        user = super().save(commit=False)
        user.company = admin_user.company
        if commit:
            user.save()
        return user