from django import forms
from .models import Notice, Assignment

class NoticeForm(forms.ModelForm) :
    class Meta :
        model = Notice
        fields = ('title', 'text')


class AssignmentForm(forms.ModelForm) :
    class Meta : 
        model = Assignment
        fields = ('title', 'assign_file')

