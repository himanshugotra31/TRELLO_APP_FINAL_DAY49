from django import forms
from django.forms import widgets
from .models import task

# class task_form_old(forms.Form):
#     name=forms.CharField(max_length=50)
#     desc=forms.CharField(widgets=forms.Textarea)
#     created_at=forms.DateTimeInput()
#     due_date=forms.DateTimeInput()
#     # list=forms.ForeignKey(task_list, on_delete=models.CASCADE)

class task_form(forms.ModelForm):
    class Meta:
        model=task
        #fields='__all__'
        fields=['name', 'desc', 'due_date', 'list']
        widgets={'due_date': forms.DateTimeInput(attrs={'type':'datetime-local'})}

