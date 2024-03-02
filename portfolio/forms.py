from django import forms
from . import models
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ('category',)

class ProjectForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = '__all__'
        widget = [
            {'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'abstract':forms.Textarea(attrs={'class':'textareaclass'}),}
        ]

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        fields = ('first_name', 'last_name', 'username','email', 'password')
        model = User