from .models import todo
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import datetime
from django.core.exceptions import ValidationError

class todoForm(forms.ModelForm):
    class Meta:
        model = todo
        fields = '__all__'
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'start_date': forms.DateInput(attrs={'type':'date'}),
            'description': forms.Textarea(attrs={'placeholder': 'Add notes or description about this task'}),
        }

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']















        
    # def clean_due_date(self):
    #     task_due = self.cleaned_data['due_date']
    #     if task_due < datetime.date.today():
    #         raise ValidationError('Invalid due date - due date should not be in the past')
    #     return task_due
    
    # def clean_start_date(self):
    #     task_start = self.cleaned_data['start_date']
    #     if task_start > self.cleaned_data['due_date']:
    #         raise ValidationError(_('Start date can not be after the due date'))
    #     return task_start